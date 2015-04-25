from kivy.app import App
from kivy.factory import Factory
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty,ListProperty,StringProperty,NumericProperty
from kivy.core.window import Window
from valid_goals import valid_goals
import search



class PuzzleRoot(GridLayout):

    jug_a=StringProperty()
    jub_b=StringProperty()
    goal=StringProperty()
    prev_index=NumericProperty()
    search=ObjectProperty()
    steps=ListProperty()
    state_sequence=ListProperty()

    def add_jug_a(self,butt,loaded,menu,drop):


        btn1=ObjectProperty()
        self.ids.drop1.open(butt)

        if loaded!="done":

            for i in range(1,11):





                btn1=Factory.Nums_juga()
                btn1.text=str(i)
                btn1.drop=str(menu)
                btn1.background_color=[25,1,100,.2]
                btn1.color=0,0,0,1

                self.ids.drop1.add_widget(btn1)

                # a.add_widget(btn1)
                butt.loaded="done"


    def add_jug_b(self,butt,loaded,menu,drop):


        btn1=ObjectProperty()
        self.ids.drop2.open(butt)

        if loaded!="done":

            for i in range(1,11):
                btn1=Factory.Nums_jugb()
                btn1.text=str(i)
                btn1.drop=str(menu)
                btn1.background_color=[25,1,100,.2]
                btn1.color=0,0,0,1
                self.ids.drop2.add_widget(btn1)


                butt.loaded="done"


    def add_goal(self,butt,loaded,jug_a,jug_b):


        btn1=ObjectProperty()


        print int(jug_a)
        print int (jug_b)

        self.ids.drop3.clear_widgets()
        self.ids.drop3.open(butt)
        for i in valid_goals(int(jug_a),int(jug_b)):
            btn1=Factory.Nums_goal()
            btn1.text=str(i)
            btn1.background_color=[25,1,100,.2]
            # btn1.drop=str(menu)
            btn1.color=0,0,0,1
            self.ids.drop3.add_widget(btn1)


            butt.loaded="done"

    def start(self,jug_a,jug_b,goal,button,status,index):

        print status
        if status=="Start again":
            button.status="Finish"
        elif status=="Finish":

            button.text="Start"
            # self.ids.stack1.clear_widgets()
            # self.ids.stack2.clear_widgets()
            self.search=search.Searches(jug_a,jug_b,goal)
            result=self.search.breadth_first()
            self.steps=result["steps"]
            self.state_sequence=result["state sequence"]
            button.status="on process"
            self.ids.jug_a.disabled=True
            self.ids.jug_b.disabled=True
            self.ids.goal.disabled=True



        else:


            if index<len(self.state_sequence):
                print index
                button.text="Next"
                _steps=Factory.Steps()
                _steps.text=str(self.steps[index])

                _status=Factory.Status()
                _status.children[1].text="Jug A: " + str(self.state_sequence[index][0])
                _status.children[0].text="Jug B: " + str(self.state_sequence[index][1])

                self.ids.stack1.add_widget(_steps)
                self.ids.stack2.add_widget(_status)

                button.index=index+1



            elif index==len(self.state_sequence):
                _final=Factory.Steps()
                _final.text="CONGRATULATIONS!!! YOU HAVE REACHED YOUR GOAL."
                __final=Factory.Status()

                _final.background_color=[1,0,0,.3]
                __final.children[1].background_color=[1,0,0,.3]
                __final.children[0].background_color=[1,0,0,.3]


                self.ids.stack1.add_widget(_final)
                self.ids.stack2.add_widget(__final)



                button.index=index+1
                button.text="Start Again?"


                button.background_color=[0,10,0,.3]
                print "here"

            elif index==len(self.state_sequence)+1:
                button.background_color=[0,10,0,.2]

                self.ids.jug_a.disabled=False
                self.ids.jug_b.disabled=False
                self.ids.goal.disabled=False

                button.text="Start"
                # button.text="Start Again??"
                print "ah"
                self.ids.stack1.clear_widgets()
                self.ids.stack2.clear_widgets()
                self.ids.jug_a.text="Jug A"
                self.ids.jug_b.text="Jug B"
                self.ids.goal.text="Goal"
                button.status="Start again"


                button.index=0









    def table(self,butt):
        if butt.text=="Table":
            butt.text="Back"
            self.ids.lbl_table.text=self.search.display_table
            self.ids.car.load_next()


        else:
            butt.text="Table"
            self.ids.car.load_previous()

    def highlight(self,butt,parent,initial_index):


        if self.prev_index is not None:
            self.ids.stack1.children[self.prev_index].background_color=[0,0,0,1]
            for i in self.ids.stack2.children[self.prev_index].children:
                i.background_color=[0,0,0,1]


        self.prev_index=initial_index




        butt.background_color=[0,0,1,.3]
        index=parent.children.index(butt)

        self.ids.stack2.children[index].children[0].background_color=[0,0,1,.3]
        self.ids.stack2.children[index].children[1].background_color=[0,0,1,.3]

class PuzzleApp(App):
    pass


if __name__=='__main__':
    Window.size=(1050,750)
    PuzzleApp().run()
