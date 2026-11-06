/**
 * Circulo usando Composição ao invés de Herança
 */
public class circuloComposicao {
    private double raio;
    private ponto centro; // O círculo "tem um" Ponto (Composição)

    public circuloComposicao() {
        this.raio = 0;
        this.centro = new ponto(); // Inicializa um ponto padrão (0,0)
    }

    public circuloComposicao(double raio, int xc, int yc) {
        this.raio = (raio > 0) ? raio : 0;
        this.centro = new ponto(xc, yc); // Cria o ponto com as coordenadas recebidas
    }

    public double getRaio() {
        return this.raio;
    }

    public void setRaio(double raio) {
        if (raio > 0)
            this.raio = raio;
        else
            this.raio = 0;
    }

    public double calcularArea() {
        return Math.PI * Math.pow(this.raio, 2);
    }

    // Na composição, precisamos acessar as informações do objeto composto
    @Override
    public String toString() {
        // Delegamos a impressão do centro para o toString do próprio objeto Ponto
        return "raio: " + this.raio + " Centro: " + this.centro.toString();
    }
}
