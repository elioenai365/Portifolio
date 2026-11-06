import java.util.Scanner;
import java.time.Year;//declaração de importação que trata o processamento de anos do caledário



public class Fundamentos {
    public static void main (String[] args) {

        // Inicializa o scanner para ler a entrada do sistema
        Scanner scanner = new Scanner(System.in);

        //recebe o nome
        System.out.print("Digite seu nome");
        String nome = scanner.nextLine();

        //recebe o ano
        System.out.print("Digite seu ano de Nascimento");
        int anoNascimento = scanner.nextInt();

        //pega o ano atual automaticamente
        int anoAtual = Year.now().getValue();

        //calcula a idade
        int idade = anoAtual - anoNascimento;

        //imprimir a msg formatada
        System.out.println("Óla"+ nome +" você tem " + idade + "  anos");

        // Fecha o recurso do scanner
        scanner.close();
    }
}
