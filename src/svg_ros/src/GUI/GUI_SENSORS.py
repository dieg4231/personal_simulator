#!/usr/bin/python




#ROS Libraries
import rospy
from svg_ros.srv import *
from std_msgs.msg import String

import thread
from Tkinter import *
import ttk





class PLANNER(object):
	def node( self,threadName, delay):
		root = Tk()
		root.withdraw() 
		root.title("Environment Configuration")

		mainframe = ttk.Frame(root, padding="3 3 12 12")
		mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		mainframe.columnconfigure(0, weight=1)
		mainframe.rowconfigure(0, weight=1)
		
		self.var_laser = IntVar()
		self.var_light = IntVar()
		self.var_base  = IntVar()
		self.var_invert= IntVar()

		laser = ttk.Checkbutton(mainframe, text='Laser Sensor', variable=self.var_laser, command=self.get_laser_flag,onvalue='1', offvalue='0')
		laser.instate(['alternate'])
		laser.grid(column=1, row=1, sticky=(W, E))
	
		light = ttk.Checkbutton(mainframe, text='Light Sensor', variable=self.var_light, command=self.get_light_flag,onvalue='1', offvalue='0')
		light.instate(['alternate'])
		light.grid(column=1, row=3, sticky=(W, E))
	
		base = ttk.Checkbutton(mainframe, text='TurtleBot', variable=self.var_base, command=self.get_base_flag,onvalue='1', offvalue='0')
		base.grid(column=1, row=4, sticky=(W, E))

		base = ttk.Checkbutton(mainframe, text='Inverted sensor', variable=self.var_invert,command=self.get_invert_flag,onvalue='1', offvalue='0')
		base.grid(column=1, row=5, sticky=(W, E))

		base.instate(['alternate'])
	
		for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
		
		
		root.geometry("400x130+%d+%d" % (460,290))
		root.wm_deiconify() #mostramos la ventana en su sitio
		root.mainloop()


	def get_laser_flag(self):
	    try:
	        print self.var_laser.get()
	    except ValueError:
	        pass
	def get_light_flag(self):
	    try:
	        return self.var_light.get()
	    except ValueError:
	        pass
	def get_base_flag(self):
	    try:
	        return self.var_base.get()
	    except ValueError:
	        pass
	def get_invert_flag(self):
	    try:
	        return self.var_invert.get()
	    except ValueError:
	        pass

	def send_values(self,req):
		resp=EnvironmentSrvResponse()
		resp.sensor= (int)( self.var_laser.get()  )
		resp.light = (int)( self.var_light.get()  )
		resp.base  = (int)( self.var_base.get()   )
		resp.invert= (int)( self.var_invert.get() )
		return resp



	def __init__(self):

		thread.start_new_thread( self.node,("Thread-1",1, ) )
		rospy.init_node('Environment_flags')
		s = rospy.Service('environment', EnvironmentSrv, self.send_values)
		rospy.spin()

		
		


if __name__ == '__main__':

	
	gui_planner = PLANNER()
	
	