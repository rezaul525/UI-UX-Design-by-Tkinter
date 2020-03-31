# start code here
import tkinter as tk #tk  is refer of tkinter
from tkinter import ttk
from csv import DictWriter
import os
root = tk.Tk()
root.configure(bg='skyblue')
root.title('INFORMATION APP') #FOR CHANGING THE NAME OF TITLE

#label_Frame for the app
# <--- Label Frame--->
label_frame = ttk.LabelFrame(root, text='Please Enter Your Details Here')
label_frame.grid(row=0,column=0, padx=5, pady=5)


# <-----All Label Box----->
lbl = ['Please Enter Your Name : ' ,'Please Enter Your Age : ','Please Enter Your Email : ','Please Select Your Gender : ']
for i in range(len(lbl)):
    f_lbl = 'Label' + str(i)
    f_lbl = ttk.Label(label_frame, text= lbl[i], font='Times')
    f_lbl.grid(row=i, column=0, sticky=tk.W, padx=2,pady=2)
    
# <---- End of Label Box----->

# <---Entry Box start for Name--->
store_nam = tk.StringVar()
nam_var = ttk.Entry(label_frame, width=20, textvariable=store_nam,font='Italic')
nam_var.focus()
nam_var.grid(row=0, column=1,padx=2,pady=2)
#  <---- Entry Box for Name---->

# <--- Entry Box Of Age-->
store_boyos = tk.IntVar()
boyos_var = ttk.Entry(label_frame, width=20, textvariable= store_boyos,font='Italic')
boyos_var.grid(row=1, column=1,padx=2,pady=2)
# <--- End of Age EntryBox--->

# <--- Entry Box of Email--->
store_email = tk.StringVar()
email_var = ttk.Entry(label_frame, width=20, textvariable= store_email, font='Italic')
email_var.grid(row=2, column=1,padx=2,pady=2)
# <---End of Entry Box---->

# <--- Start of Combo Box--->
store_gender = tk.StringVar()
gender_combo = ttk.Combobox(label_frame, width=20, state='readonly', font='Italic') #state for something showing on box like 'male' 
gender_combo['values'] = ('Male', 'Female', 'Others')
gender_combo.current(0)
gender_combo.grid(row=3, column=1,padx=2,pady=2)
# <---End of Combo Box--->

# <--- Start of Radio Box--->
label_frame2 = ttk.LabelFrame(root, text='Please Mark Your Profession From Below')
label_frame2.grid(row=1,column=0, padx=5, pady=5)
store_usertype = tk.StringVar()

# <--- Start of First Radio--->
first_radio = ttk.Radiobutton(label_frame2, text='STUDENT', value='STUDENT', variable= store_usertype)
first_radio.grid(row=4, column= 0, sticky=tk.W)
# <--- End of First Radio--->

# <--- Start of Second Radio--->
second_radio = ttk.Radiobutton(label_frame2, text='TEACHER' , value='TEACHER', variable= store_usertype)
second_radio.grid(row=4, column=1, sticky=tk.W)
# <--- End of Second radio--->

# <--- Start of 3rd Radio--->
third_radio = ttk.Radiobutton(label_frame2,variable= store_usertype, text='STAFF', value='STAFF',)
third_radio.grid(row=5, column=0, sticky=tk.W)
# <---End of Radio --->

# <---Start 4th Radio--->
fourth_radio = ttk.Radiobutton(label_frame2,variable= store_usertype, text='OTHERS', value='OTHERS',)
fourth_radio.grid(row=5, column=1, sticky=tk.W)
# <---End of 4th radio--->
# <--- end of Radio Box--->

# <--- Check Button Start---->
label_frame3 = ttk.LabelFrame(root, text='If Nedded Subscribe Us')
label_frame3.grid(row=2,column=0, padx=5,pady=5, sticky=tk.W)

store_check = tk.IntVar()
check_var = ttk.Checkbutton(label_frame3, text='Please check to subscribe\t Thank you very much !!!',variable=store_check)
check_var.grid(row=6, columnspan=5, sticky= tk.W)
# <--- Check Button End---->


# <---- Function Start Here---->
def sub_action():
    user_name = nam_var.get()
    user_age = boyos_var.get()
    user_email = email_var.get()
    # print(f'{user_name} {user_age} {user_email}') # <--- For import the output on txt document--->
    user_gender = gender_combo.get()
    user_type = store_usertype.get()
    
    if store_check.get()== 0:
        Subscribed ='No'
    else:
        Subscribed = 'Yes'

    # <--- For import the output on txt document--->

    # print(f'{user_name} is a {user_gender} {user_type} age {user_age}  and his/her email address is --> {user_email}  Did He/She Subscribe? {Subscribed}')

    # with open('file.txt', 'a') as f:
    #     f.write(f'{user_name},{user_age},{user_email},{user_gender},{user_type},{Subscribed}\n')

        # <--- For import the output on txt document--->

# # <----- Creating a csv file----->
    with open('mynew.csv', 'a', newline='') as f:
        d_write = DictWriter(f, fieldnames=['User Name', 'User Age','User Email','User Gender','User Type','Subscribed'])

        if os.stat('mynew.csv').st_size==0: #for repeating output follow os module
            d_write.writeheader() 
            

        d_write.writerow({
            'User Name': user_name,
            'User Age': user_age,
            'User Email': user_email,
            'User Gender': user_gender,
            'User Type' : user_type,
            'Subscribed':  Subscribed
        })

    nam_var.delete(0, tk.END) #Here (END) is a global variable
    boyos_var.delete(0, tk.END)
    email_var.delete(0, tk.END)

    # <--- Function End --->

# <--- Start of button--->
label_frame4 = ttk.LabelFrame(root, text='Submit Your Details By Clicking "SUBMIT"')
label_frame4.grid(row=4,column=0, padx=5,pady=5, sticky=tk.W)
# label_frame4.configure(='yellow')

submit_btn = ttk.Button(label_frame4, text='SUBMIT', command= sub_action)
submit_btn.grid(row=7, column=0, sticky=tk.W,padx=2,pady=2)
# <--- End of Button--->
root.mainloop()

# <----------------------------------- END OF PROJECT/CODE--------------------------->

