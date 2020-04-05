import tkinter as tk
import pandas as pd
from classification import classifier_creator
import threading



class ClassifierApp(tk.Tk):
    title_font = ('courier 10 pitch', 30)
    normal_font = ('courier 10 pitch', 20)
    small_font = ('courier 10 pitch', 15)
    prediction = ''

    def __init__(self):
        super().__init__()
        self.geometry('650x650')
        self.title('Classificador de questões')
        self.initialize_widgets()
        print('Please wait while the classifier is being created!')
        self.classifier = classifier_creator(min_df=11)

    def initialize_widgets(self):
        self.app_title = tk.Label(self, text='Classificador de questões',
         font=self.title_font)

        instructions_text = 'Digite a questão e clique em começar para receber o resultado'
        self.instructions = tk.Label(self, text=instructions_text, wraplength=600,
         justify=tk.CENTER, font=self.normal_font)

        self.input_widget = tk.Text(self, width=42, height=10, font=self.small_font,
         wrap=tk.WORD)
        

        self.start_button = tk.Button(self, text='Começar', font=self.normal_font,
         command=self.question_classifier)

        self.result_widget_output = tk.Label(self, font=self.normal_font,
        text='A matéria da questão provavelmente é:')

        self.result_str = tk.Label(self, text='')

        self.app_title.pack(side=tk.TOP, pady=(0, 50)) 
        self.instructions.pack(side=tk.TOP)
    
        self.input_widget.pack(side=tk.TOP, pady=20)
        self.start_button.pack(side=tk.TOP)

        self.wait_label = tk.Label(self, text='Por favor, aguarde enquanto seu texto está sendo processado',
        font=self.small_font, fg='blue', wraplength=600)

    
    def question_classifier(self):
        
        self.input_text = self.input_widget.get(1.0, tk.END).strip()
        self.result_str.pack_forget()
        self.result_widget_output.pack_forget()

        if len(self.input_text) > 0:
            self.wait_label.pack()
            self.prediction = self.classifier(self.input_text)
            self.result_str = tk.Label(self, text=self.prediction[0], font=self.title_font, fg='red')
            self.wait_label.pack_forget()
            self.result_widget_output.pack()
            self.result_str.pack()
            


if __name__ == "__main__":
    root = ClassifierApp()
    root.mainloop()