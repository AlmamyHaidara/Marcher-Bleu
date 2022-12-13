public class Point {
    private float x;
    private float y;
    private float rayon;
    private final double pi = Math.PI;

    public Point(float x, float y, float rayon){
        this.x = x;
        this.y = y;
        this.rayon = rayon;
    }

    public void AffichePoint(){
        System.out.println("POINT("+this.x+","+this.y+")");
    }
    public double getPerimetre(){
        return 2*(pi) * this.rayon;
    }
    public double getSurface(){
        return pi * Math.pow(this.rayon,2);
    }
    public void AfficherCercle(){
        System.out.println("CERCLE("+this.x+","+this.y+","+this.rayon+")");
    }
    public double distance(double x, double y){
        return Math.sqrt(Math.pow(x-this.x,2)+
                Math.pow(y-this.y, 2));
    }

    public boolean appartenir (double x, double y){
        if(this.distance(x,y) == this.rayon){
            return true;
        }else {
            return false;
        }
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }

    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
}
