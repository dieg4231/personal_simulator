/********************************************************
 *      potential_fields.h                    	*
 *		Diego Cordero				*
 *		FI-UNAM					*
 *		22-3-2018                               
********************************************************/
#include <math.h>
#define ALPHA 1

void surround(coord coord_robot,coord coord_dest,Raw observations,int num_sensors,float largest_value,float origen,float range_sensor,float *angle)
{
    //printf("num_sensors: %d \n largest_value: %f\norigen: %f\nrange_sensor: %f\nquantized_intensity: %d\nquantized_attraction:%d\n",num_sensors,largest_value,origen,range_sensor,quantized_intensity,quantized_attraction);
    int i;
    float step=range_sensor/num_sensors; /*4.1818/100=0.04188*/
    float x=0;
    float y=0;
    float magnitud;
    float theta,xc;
    /*Suma de los vectores de los sensores y se ubican en el cuadrante adecuado
    donde el origen es el robot el robot esta siempre viendo hacia el eje Y positivo */
    for ( i=0, theta=origen; i < num_sensors; i++, theta+=step )
        if (observations.sensors[i] < largest_value)
        {
            y+= fabs( ALPHA * observations.sensors[i] * sin(theta) );
            xc= fabs( ALPHA * observations.sensors[i] * cos(theta) );
            x += (theta >= 0) ? xc : -xc;
        } 
    /*Modulo de los vectores de repulsion*/
    /*Vector  unitario de repulcion*/
    if (magnitud=sqrt(pow(x,2)+pow(y,2)))
    {   
        x/=magnitud;
        y/=magnitud;
    }
         
    /*Transformamos el angulo en el angulo que el robot debe girar*/
    theta = atan2(y, x);
    if (theta > M_PI/2 || theta <= -M_PI/2)
        theta -=M_PI / 4;
    else if (*angle < 0)
        theta +=M_PI / 4;

    if(theta==0)
        *angle =0;
    else if (theta > 0 && theta <= M_PI)
        *angle = theta - M_PI / 2; 
    else if (theta < - M_PI / 2)   
        *angle= 3 * M_PI / 2 + theta;
    else if(theta < 0)
        *angle = theta - M_PI / 2;
    else
        printf("ERROR\n"); 


    printf("ANGLE_ %f\n",*angle); 
    
              
}


















/*Suma de los vectores de los sensores y se ubican en el cuadrante adecuado
donde el origen es el robot el robot esta siempre viendo hacia el eje Y positivo */
/*for( i=0, theta=origen; i < num_sensors; i++, theta+=step )
    if(observations.sensors[i] < largest_value)
    {
        if(theta>0)
            x-=fabs(ALPHA*observations.sensors[i]*cos(theta));
        else
            x+=fabs(ALPHA*observations.sensors[i]*cos(theta));

        if( theta > -M_PI/2 && theta < M_PI/2 )
            y+=fabs(ALPHA*observations.sensors[i]*sin(theta));
        else
            y-=fabs(ALPHA*observations.sensors[i]*sin(theta));        
    }  
     ////////////////////////////////7   
        
if(x >= 0 && y >= 0)
    x*=-1;
else if( x < 0 && y >= 0)
    x*=-1;
else if(x<0 && y<=0)
{
    x*=-1;
    y*=-1;
}
else if(x>=0 &&y<=0)
{   
    x*=-1;
    y*=-1;
}*/