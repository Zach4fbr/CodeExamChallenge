//e1.c

#include <stdio.h>
#include <stdlib.h>

#define NOM_FIC_TRAINS  "trains.txt"
#define MAX_NB_TRAINS   100
#define LG_NOM_VILLE    20

typedef struct
{
  int heu, min;
} Horaire;

typedef struct
{
  char ville[LG_NOM_VILLE];
  Horaire horaire;
} Train;

// les trains sont stockes dans un tableau, les fonctions recoivent l'adresse
// du tableau et le nombre de trains

int lireFicTrains(Train *trains);
void trierTrains(Train *trains, int nbTrains);
int chercherTrainMax(Train *trains, int nbTrains);
int comparerHoraires(Horaire *horaire1, Horaire *horaire2);
void echangerTrains(Train *trains, int indiceTrain1, int indiceTrain2);
void ecrireFicTrains(Train *trains, int nbTrains);

// lit le fichier et range les donnees dan le tableau trains, retourne le
// nombre de trains lus
int lireFicTrains(Train *trains)
{
  FILE *fic;
  Train trainLu;
  int nbTrains = 0;

  fic = fopen(NOM_FIC_TRAINS, "r");
  if (fic == NULL)
  {
    printf("lecture fichier: erreur ouverture\n");
    exit(1);
  }

  while (fscanf(fic, "%s%d%d", trainLu.ville, &trainLu.horaire.heu,
                                                &trainLu.horaire.min) == 3)
  {
    trains[nbTrains] = trainLu;
    nbTrains++;
  }

  fclose(fic);
  return nbTrains;
}

void trierTrains(Train *trains, int nbTrains)
{
  int n;
  int indiceTrainMax;

  // tri par selection : on cherche le max et on le met a la fin du tableau
  // par echange avec le dernier element, puis on reitere sur le tableau diminue
  // d'une unite
  for (n = nbTrains; n > 1; n--)
  {
    indiceTrainMax = chercherTrainMax(trains, n);
    echangerTrains(trains, indiceTrainMax, n - 1);
  }
}

// cherche le train d'horaire max et retourne son indice
int chercherTrainMax(Train *trains, int nbTrains)
{
  int indiceTrainMax = 0;
  int i = 0;

  for (i = 0; i < nbTrains; i++)
  {
    if (comparerHoraires(&trains[i].horaire,
                          &trains[indiceTrainMax].horaire) > 0)
      indiceTrainMax = i;
  } 

  return indiceTrainMax;
}

// retourne -1, 0, ou +1 selon que horaire1 est <, egal, ou > chronologiquement
// a horaire2
int comparerHoraires(Horaire *horaire1, Horaire *horaire2)
{
  if (horaire1->heu < horaire2->heu ||
        (horaire1->heu == horaire2->heu && horaire1->min < horaire2->min))
    return -1;
  else if (horaire1->heu > horaire2->heu ||
             (horaire1->heu == horaire2->heu && horaire1->min > horaire2->min))
    return 1;
  else
    return 0;
}

void echangerTrains(Train *trains, int indiceTrain1, int indiceTrain2)
{
  Train sauveTrain1 = trains[indiceTrain1];
  trains[indiceTrain1] = trains[indiceTrain2];
  trains[indiceTrain2] = sauveTrain1;
}

void ecrireFicTrains(Train *trains, int nbTrains)
{
  FILE *fic;
  int i;

  fic = fopen(NOM_FIC_TRAINS, "w");
  if (fic == NULL)
  {
    printf("ecriture fichier: erreur ouverture\n");
    exit(1);
  }

  for (i = 0; i < nbTrains; i++)
    fprintf(fic, "%s %d %d\n", trains[i].ville, trains[i].horaire.heu,
                                                trains[i].horaire.min);

  fclose(fic);
}

int main(void)
{
  Train trains[MAX_NB_TRAINS];
  int nbTrains;

  nbTrains = lireFicTrains(trains);
  trierTrains(trains, nbTrains);
  ecrireFicTrains(trains, nbTrains);

  return 0;
}
