// e2.c

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#define NOM_FIC_DICO  "dico.txt"
#define LG_MAX_MOT    30

// maillon de la liste chainee
typedef struct _Traduction
{
  char fra[LG_MAX_MOT];
  char ang[LG_MAX_MOT];
  struct _Traduction* suiv;
} Traduction;

typedef struct
{
  Traduction *tete;
} Dico;

void lireFicDico(Dico *dico);
void menu(Dico *dico);
void afficherDico(Dico *dico);
void choixTraduire(Dico *dico);
void choixAjouterMot(Dico *dico);
void choixSupprimerMot(Dico *dico);
void ecrireFicDico(Dico *dico);
void insererTraduction(Dico *dico, Traduction *traduction);
Traduction *chercherMot(Dico *dico, char *motFra);

// lit le fichier et cree la liste chainee
void lireFicDico(Dico *dico)
{
  FILE *fic;
  char motFra[LG_MAX_MOT], motAng[LG_MAX_MOT];
  Traduction *traduction;

  dico->tete = NULL;

  fic = fopen(NOM_FIC_DICO, "r");
  if (fic == NULL)
  {
    printf("lecture fichier: erreur ouverture\n");
    exit(1);
  }

  while (fscanf(fic, "%s%s", motFra, motAng) == 2)
  {
    traduction = (Traduction *) malloc(sizeof(Traduction));
    strcpy(traduction->fra, motFra);
    strcpy(traduction->ang, motAng);

    insererTraduction(dico, traduction);
  }

  fclose(fic);
}

void menu(Dico *dico)
{
  bool quitter = false;
  int choix;

  while (!quitter)
  {
    printf("\n");
    printf("1 afficher dictionnaire\n");
    printf("2 traduire\n");
    printf("3 ajouter mot\n");
    printf("4 supprimer mot\n");
    printf("5 enregister fichier\n");
    printf("6 quitter\n");
    printf("choix : ");
    scanf("%d", &choix);

    switch( choix)
    {
      case 1 :
        afficherDico(dico);
        break;
      case 2 :
        choixTraduire(dico);
        break;
      case 3 :
        choixAjouterMot(dico);
        break;
      case 4 :
        choixSupprimerMot(dico);
        break;
      case 5 :
        ecrireFicDico(dico);
        break;
      case 6 :
        quitter = true;
        break;
    }
  }
}

void afficherDico(Dico *dico)
{
  Traduction *traduction = dico->tete;

  while (traduction != NULL)
  {
    printf("%s : %s\n", traduction->fra, traduction->ang);
    traduction = traduction->suiv;
  }
}

void choixTraduire(Dico *dico)
{
  char motFra[LG_MAX_MOT];
  Traduction *traduction;

  printf("mot a traduire : ");
  scanf("%s", motFra);

  traduction = chercherMot(dico, motFra);
  if (traduction == NULL)
    printf("mot non trouve\n");
  else
    printf("traduction : %s\n", traduction->ang);
}

void choixAjouterMot(Dico *dico)
{
  char motFra[LG_MAX_MOT];
  Traduction *traduction;

  printf("mot a ajouter : ");
  scanf("%s", motFra);

  traduction = chercherMot(dico, motFra);
  if (traduction != NULL)
    printf("mot deja present\n");
  else
  {
    traduction = (Traduction *) malloc(sizeof(Traduction));
    strcpy(traduction->fra, motFra);

    printf("traduction : ");
    scanf("%s", traduction->ang);

    insererTraduction(dico, traduction);
  }
}

void choixSupprimerMot(Dico *dico)
{
  char motFra[LG_MAX_MOT];
  Traduction *traduction;
  Traduction *prec;

  printf("mot a supprimer : ");
  scanf("%s", motFra);

  // parcours de la liste a la recherche du mot en gardant trace du maillon
  // precedent
  traduction = dico->tete;
  prec = NULL;
  while (traduction != NULL && strcmp(motFra, traduction->fra) != 0)
  {
    prec = traduction;
    traduction = traduction->suiv;
  }

  if (traduction == NULL)
    printf("mot non trouve\n");
  else
  {
    // retirer le maillon du chainage
    if (prec == NULL)   // le maillon a supprimer est le premier
      dico->tete = traduction->suiv;
    else  // on retire le maillon en chainant son precedent a son suivant
      prec->suiv = traduction->suiv;

    free(traduction);
  }
}

void ecrireFicDico(Dico *dico)
{
  FILE *fic;
  Traduction *traduction;

  fic = fopen(NOM_FIC_DICO, "w");
  if (fic == NULL)
  {
    printf("ecriture fichier: erreur ouverture\n");
    exit(1);
  }

  traduction = dico->tete;
  while (traduction != NULL)
  {
    fprintf(fic, "%s %s\n", traduction->fra, traduction->ang);
    traduction = traduction->suiv;
  }

  fclose(fic);
}

void insererTraduction(Dico *dico, Traduction *traduction)
{
  // insertion en tete
  traduction->suiv = dico->tete;
  dico->tete = traduction;
}

// cherche un mot francais dans le dictionnaire et retourne son maillon ou NULL
// si non trouve
Traduction *chercherMot(Dico *dico, char *motFra)
{
  Traduction *traduction = dico->tete;

  while(traduction != NULL && strcmp(motFra, traduction->fra) != 0)
    traduction = traduction->suiv;

  return traduction;
}

int main(void)
{
  Dico leDico;

  lireFicDico(&leDico);
  menu(&leDico);

  return 0;
}
