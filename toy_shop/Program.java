package intermediate_control_work.toy_shop;

import java.util.ArrayList;

public class Program {
    private static ArrayList<String> candidate = new ArrayList<>(); // Список кандидатов на выигрыш

    public static void main(String[] args) {
        ToysGenerate a = new ToysGenerate(10);
        ToysLottery x = new ToysLottery(a.getList());
        candidateGenerate(10);

        printList(x.getList());
        System.out.println(x.getList().size());

        for (int i = 0; i < candidate.size(); i ++) {
            String round = String.format("%s выиграл %s", candidate.get(i), x.lotteryNow());
            System.out.println(round);
        }

        printList(x.getList());
        System.out.println(x.getList().size());
    }

    public static void candidateGenerate(int size) {
        for ( int i = 0; i < size; i ++) {
            candidate.add(String.format("Участник-%d", i));
        }
    }

    public static void printList(ArrayList<Toy> array) {
        for (Toy elm : array) {
                System.out.println(elm.getId());
                System.out.println(elm.getName());
                System.out.println(elm.getAmount());
                System.out.println(elm.getDrop());
                System.out.println();
            }
    }
}
