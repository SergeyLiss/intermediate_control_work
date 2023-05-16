package intermediate_control_work.toy_shop;

public class ToysLottery {
    ArrayList<Toy> listToys; // Список игрушек
    double stepDropAllToys; // Сумма частот выпадения игрушек

    public ToysLottery(ArrayList<Toy> listToysIn){
        this.listToys = listToysIn;
        stepSum();
    }

    public static void stepSum() {
        for (Toy toyElm : listToys) {
            this.stepDropAllToys += toyElm.getDrop();
        }
    }

    @Override
    public static void stepSum() {
        for (Toy toyElm : listToys) {
            this.stepDropAllToys += toyElm.getDrop();
        }
    }

}
