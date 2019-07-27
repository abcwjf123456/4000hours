# 传递列表
# 如果不想让列表传递后为空可以创建列表副本传递给函数例：function_name(list_name[:])切片表示法[:]创建副本

def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print(current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """模拟打印好的模型"""
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
