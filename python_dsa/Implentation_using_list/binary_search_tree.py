'''
binary search tree:
operations -> 1.inserting/adding data  2.searching data 3. inorder accessing  4.preorder acceessing  5. postorder accessing 6. deleting data
'''
class Node:
    def __init__(self, data = 0):
        if data == 0:
            data = int(input('Enter data of the node: '))
        self.left = None
        self.data = data
        self.right = None
    
class BST:
    
    def __init__(self):
        self.root = None

    def add_node(self,data):
        new_node = Node()
        if self.root == None:
            self.root = new_node
        
        temp1 = self.root
        temp2 = None

        while temp1 != None:
            temp2 = temp1
            if new_node < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if new_node.data < temp2.data:
            temp2.left = new_node
        else:
            temp2.right = new_node

    def in_order_access(self, temp):
        if temp == None:
            return
        
        self.in_order_access(temp.left)
        print(temp.data, end = '  ')
        self.in_order_access(temp.right)


    def pre_order_access(self, temp):
        if temp != None:
            print(temp.data, end = '   ')
            self.pre_order_access(temp.left)
            self.pre_order_access(temp.right)

        
    def post_order_access(self, temp):
        if temp == None:
            return
        self.post_order_access(temp.left)
        self.post_order_access(temp.right)
        print(temp.data, end = '  ')
    
    def search_node(self, temp, search_data):
        found = False
        if temp != None:
            if temp.data == search_data:
                return True
            found = self.search_node(temp.left, search_data)
            if found:
                return found
            found = self.search_node(temp.right, search_data)
        return found

        
    
    def delete_node(self, temp, delete_data):
        if temp == None:
            return

class Menu:
    def __init__(self):
        self.choice = 0
    
    def is_tree_empty(self, bst):
        if bst.root == None:
            print('Tree is empty')
            return True
        return False
    

    def  menu(self, bst):
        
        
        match self.choice:
            case 1 : bst.add_node()
            case 2 :
                if self.is_tree_empty(bst):
                    return
                search_data
                bst.search_node()
            case 3 : bst.in_order_access()
            case 4 : bst.pre_order_access()
            case 5 : bst.post_order_access()
            case 6 : bst.delete_node()
            case 7 : break
            case _ : print("select valid choice ")
Menu.menu()
