class Employee:
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.template = None  
    
    def attach_template(self, template_name):
        self.template = template_name
        print(f"Template '{template_name}' attached to Employee {self.emp_id}: {self.emp_name}")


class SalaryManagement:
    def __init__(self):
        self.templates = {}
    
    def add_template(self, template_name, details):
        self.templates[template_name] = details
        print(f"Template '{template_name}' added with details: {details}")
    
    def attach_template_to_employee(self, employee, template_name):
        if template_name in self.templates:
            employee.attach_template(template_name)
        else:
            print(f"Template '{template_name}' not found in the system.")
