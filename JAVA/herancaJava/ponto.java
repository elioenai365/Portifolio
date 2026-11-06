public class ponto {

    protected int x, y;

    public ponto() {
        x = 0;
        y = 0;

    }

    public ponto(int xc, int yc) {

        x = xc;
        y = yc;
    }

    public String toString() {
        return ("(" + x + "," + y + ")");
    }
}