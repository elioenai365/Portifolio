public class circulo extends ponto {
    protected double raio;

    public circulo() {
        setRaio(0);
    }

    public circulo(double raio, int xc, int yc) {
        super(xc, yc); // chama o construtor de ponto
        setRaio(raio);
    }

    // Exercicio 1: Método getRaio
    public double getRaio() {
        return this.raio;
    }

    public void setRaio(double raio) {
        if (raio > 0)

            this.raio = raio;
        else
            this.raio = 0;
    }

    // Exercicio 2: Método para proporcionar a área do Circulo
    public double calcularArea() {
        return Math.PI * Math.pow(this.raio, 2);

    }

    // Exercicio 3: Rescrita do to String acessando x e y diretamente (protected)
    @Override
    public String toString() {
        // como x e y são protected em Ponto, circulo tem acesso direto a eles
        return "raio:" + this.raio + "Centro: (" + this.x + "," + this.y + ")";
    }
}
