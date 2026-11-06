public class testarCirculo {
    public class TestaCirculo {
        public static void main(String[] xyz) {
            circulo c1 = new circulo(5.0, 10, 20);

            // Testando o toString modificado
            System.out.println("Dados do Circulo c1 -> " + c1);

            // Testando o Exercício 1 (getRaio)
            System.out.println("Raio obtido via getter: " + c1.getRaio());

            // Testando o Exercício 2 (Área)
            System.out.printf("Área do círculo: %.2f\n", c1.calcularArea());
        }
    }
}
