package intermediate_control_work.toy_shop;

public class Toy {
    private int id;                 // Id
    private String name;            // Название игрушки
    private double amount;          // Количество
    private double dropChance;   // Частота выпадения игрушки

    public void setId(int id) { this.id = id;}
    public void setName(String name) { this.name = name;}
    public void setAmount(double amount) { this.amount = amount;}
    public void setDrop(double drop) { this.dropChance = drop;}

    public int getId() { return this.id;}
    public String getName() { return this.name;}
    public double getAmount() { return this.amount;}
    public double getDrop() { return this.dropChance;}
}
