package intermediate_control_work.toy_shop;

import java.util.ArrayList;
import java.util.Random;

public class ToysLottery {
    private static ArrayList<Toy> listToys = new ArrayList<>(); // Список игрушек
    private static double stepDropAllToys = 0.0; // Сумма частот выпадения игрушек

    public ToysLottery(ArrayList<Toy> listToysIn){
        listToys = listToysIn;
        stepSum();
    }

    public static void stepSum() {
        for (Toy toyElm : listToys) {
            stepDropAllToys += toyElm.getDrop();
        }
    }

    public double getDropAll() { return stepDropAllToys;}

    public String lotteryNow() {
        Random variable = new Random();
        double constemp = variable.nextDouble();
        double chance = stepDropAllToys * constemp;
        double temp = 0.0;

        for (int i = 0; i < listToys.size(); i ++) {
            temp += listToys.get(i).getDrop();
            if (temp > chance) {
                Toy win = listToys.get(i);
                if (win.getAmount() > 1.0) {
                    win.setAmount(win.getAmount() - 1.0);
                    listToys.add(i, win);
                }
                else {
                    ArrayList<Toy> rok1 = new ArrayList<Toy>(listToys.subList(0, i));
                    ArrayList<Toy> rok2 = new ArrayList<Toy>(listToys.subList((i+1), listToys.size()));
                    listToys = new ArrayList<>(rok1);
                    listToys.addAll(rok2);
                    System.out.print(listToys);
                    chance -= constemp * win.getDrop();
                }
                return win.getName();
            }
        }
        return "Error LotteryNow()... for";
    }

    public ArrayList<Toy> getList() { return listToys;}
}
