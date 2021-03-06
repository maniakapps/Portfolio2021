package com.maniakapps;
public class Plot {



    private int x;

    private int y;

    private int width;

    private int depth;



    public Plot()

    {

        x=0;

        y=0;

        width=0;

        depth=0;

    }



    public Plot(int x, int y,int depth, int width)

    {

        this.x = x;

        this.y = y;

        this.depth = depth;

        this.width = width;



    }



    public Plot(Plot other)

    {

        x = other.x;

        y = other.y;

        depth = other.depth;

        width = other.width;

    }



    public void setX(int x)

    {

        this.x = x;

    }



    public void setY(int y)

    {

        this.y = y;

    }



    public void setDepth(int depth)

    {

        this.depth = depth;

    }

    public void setWidth(int width)

    {

        this.width = width;

    }

    public boolean overlaps(Plot plot)
    {
        if((this.x + this.width) <= plot.x
                || this.x >= (plot.x + plot.width)){
            return false;
        }
        if((this.y + this.depth) <= plot.y
        || this.y >= (plot.y + plot.depth)){
            return false;
        }
        return true;
    }
    /*
    public boolean overlaps(Plot plot)

    {

        if(((x>=plot.x && x <= (plot.x+plot.width)) && (y >=plot.y && y <= (plot.y+plot.depth))) ||

                (((x + width)>=plot.x && (x+width) <= (plot.x+plot.width)) && (y >=plot.y && y <= (plot.y+plot.depth))) ||

                ((x>=plot.x && x <= (plot.x+plot.width)) && ((y +depth) >=plot.y && (y+depth) <= (plot.y+plot.depth))) ||

                (((x+width)>=plot.x && (x+width) <= (plot.x+plot.width)) && ((y+depth) >=plot.y && (y+depth) <= (plot.y+plot.depth))))



            return true;



        else if(((plot.x>=x && plot.x <= (x+width)) && (plot.y >=y && plot.y <= (y+depth))) ||

                (((plot.x + plot.width)>=x && (plot.x+plot.width) <= (x+width)) && (plot.y >= y && plot.y <= (y+depth))) ||

                ((plot.x>=x && plot.x <= (x+width)) && ((plot.y +plot.depth) >= y && (plot.y+plot.depth) <= (y+depth))) ||

                (((plot.x+plot.width)>=x && (plot.x+plot.width) <= (x+width)) && ((plot.y+plot.depth) >= y && (plot.y+plot.depth) <= (y+depth))))

            return true;



        return false;





    }
    */




    public boolean encompasses(Plot plot)

    {

        if(plot.x >= x
                && plot.x <= x + width
                && plot.y >= y
                && plot.y <= y + depth
                && plot.x + plot.width >= x
                && plot.x + plot.width <= x + width
                && plot.y <= y + depth)

            return true;

        return false;

    }



}