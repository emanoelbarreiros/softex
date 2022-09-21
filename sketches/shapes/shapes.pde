ArrayList<Polygon> poligonos;

void setup() {
  size(600, 600);
  poligonos = new ArrayList<Polygon>();
  poligonos.add(new Triangle(10,10, 400,10, 200,300));
  
}

void update() {
  // nada por enquanto
}

void draw() {
  
  background(200);
  
  for (Polygon p : poligonos) {
    p.draw();
  }
  
}
