export interface anime {
  id: number;
  title: string;
  rating: number;
  image: string;
}

export interface match {
  anime1: anime;
  anime2: anime;
}
