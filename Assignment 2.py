from functools import wraps

# -------------------------------
# Decorators for Formatting
# -------------------------------

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


def bordered(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        content = func(*args, **kwargs)
        border = "=" * 50
        return f"{border}\n{content}\n{border}"
    return wrapper


# -------------------------------
# Report Class
# -------------------------------

class Report:
    template = "Default Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Magic Method: String Representation
    def __str__(self):
        return f"{self.template}\nTitle: {self.title}\n\n{self.content}"

    # Magic Method: Report Length
    def __len__(self):
        return len(self.content)

    # Magic Method: Combine Reports
    def __add__(self, other):
        new_title = f"{self.title} + {other.title}"
        new_content = self.content + "\n\n" + other.content
        return Report(new_title, new_content)

    # Class Method: Create Template
    @classmethod
    def set_template(cls, template_name):
        cls.template = template_name

    # Decorated Report Output
    @bordered
    @uppercase
    def formatted_report(self):
        return str(self)


# -------------------------------
# Advanced Report Class
# -------------------------------

class SalesReport(Report):

    @classmethod
    def monthly_template(cls):
        cls.template = "Monthly Sales Report"

    @classmethod
    def yearly_template(cls):
        cls.template = "Yearly Sales Report"


# -------------------------------
# Example Usage
# -------------------------------

# Select a template
SalesReport.monthly_template()

# Create reports
report1 = SalesReport(
    "January Sales",
    "Revenue: $50,000\nProfit: $12,000"
)

report2 = SalesReport(
    "February Sales",
    "Revenue: $60,000\nProfit: $15,000"
)

# Display formatted report
print(report1.formatted_report())

# Report length
print("\nContent Length:", len(report1))

# Combine reports
combined = report1 + report2

print("\nCombined Report:")
print(combined.formatted_report())
