import java.text.DecimalFormat;

public class Main {
    public static void main(String[] args) {
        Point cercle = new Point(1,2,5);
        DecimalFormat df = new DecimalFormat("0.00");
        System.out.println("Le périmetre est : " + df.format(cercle.getPerimetre()));
        System.out.println("La Surface est : " + df.format(cercle.getSurface()));
        System.out.println("Appartient au cercle: "+cercle.appartenir(5,5));

    }
}