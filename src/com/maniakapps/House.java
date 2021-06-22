package com.maniakapps;

import java.text.DecimalFormat;
public class House { /*****Attributes*****/
    private String address;
    private String city;
    private String state;
    private String zipcode;
    private Realtor realtorObj;
    private float price; //private double price;
    private boolean isSold;
     /*****Constructors*****/
public House()//default
{ address = ""; city = ""; state = ""; zipcode = ""; realtorObj = new Realtor(realtorObj); price = 0; isSold = false; }
public House(String address,String city,String state,String zipcode,Realtor realtorObj,float price)//overloaded
 { this.address = address; this.city = city; this.state = state; this.zipcode = zipcode; this.realtorObj = new Realtor(realtorObj); this.price = price; this.isSold = false; }
 public House(House orig)//copy
{ this.address = orig.address; this.city = orig.city; this.state = orig.state; this.zipcode = orig.zipcode; this.realtorObj = new Realtor(orig.realtorObj); this.price = orig.price; this.isSold = false; }
/*****Accessor Methods(Getters)*****/
public String getAddress()
{ return address; }
public String getCity() { return city; }
public String getState() { return state; }
public String getZipcode() { return zipcode; }
public float getPrice() { return price; }
public Realtor getRealtor() {
    return new Realtor(realtorObj); }
public boolean getListingStatus() { return isSold; }
/*****Mutator Methods(Setters)*****/
public void setPrice(float price) { this.price = price; }
public Realtor setRealtor(Realtor realtorObj) {
    return new Realtor(realtorObj); } /* public void setRealtor(Realtor otherRealtor) { this.realtorObj = new Realtor(otherRealtor); }*/
    public void setListingStatus() { this.isSold = false; } /*****Additional Methods*****/ public boolean equals(House other) { return (this.address.equalsIgnoreCase(other.address) && this.city.equalsIgnoreCase(other.city) && this.state.equalsIgnoreCase(other.state) && this.zipcode.equalsIgnoreCase(other.zipcode) && this.realtorObj.equals(other.realtorObj) && this.price == (other.price) && this.isSold == (other.isSold)); }
    public String toString() { DecimalFormat formatter = new DecimalFormat("$##,##0.00");
        return "House Address: " + address + "\t" + city + " , " + state + zipcode + realtorObj.toString() + "\nPrice:" + formatter.format(price) + "\n" + "Price: " + price + "\nListing Status: " + isSold;
        } }