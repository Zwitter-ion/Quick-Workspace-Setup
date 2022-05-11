from tkinter import filedialog

class add_mode():
    
    def add_programs(self):

        file_and_path = filedialog.askopenfilename()
        self.file = file_and_path.split('/')[-1]
        self.path = file_and_path.split(self.file)[0]
        
    
    def save_data(self):

        mode = 'hello'
        data_file = f'Data\\{mode}.qes'

        with open('Data\\Mode_list.qes', 'a') as data_file:
            data_file.write(f'\n{mode}')
        
        with open(data_file, 'a') as data_file:
            for items in self.data_list:
                data_file.write(f'\n{items}')




if __name__ == '__main__':
    add_mode = add_mode()
    add_mode.add_programs()
