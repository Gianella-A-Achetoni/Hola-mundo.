package TercerSemestreee.Java.Leccion04.InstanceOff.domain;

public class Empleado1 {
    protected String nombre;
    protected double sueldo;
    public Empleado1(String nombre, double sueldo){
        this.nombre = nombre;
        this.sueldo = sueldo;
    }
    public String obtenerDetalle(){
        return "Nombre: " + this.nombre + ", Sueldo: " + this.sueldo;
    }
    public String getNombre(){
        return nombre;
    }
    public void setNombre(String nombre){
        this.nombre = nombre;
    }
    public double getSueldo(){
        return sueldo;
    }
    public void setSueldo(double sueldo){
        this.sueldo = sueldo;
    }
}