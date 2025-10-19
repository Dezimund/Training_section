# class Report:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#     def generate_report(self):
#         return f"Report: {self.title} \nContent: {self.content}"
#
#     def save_to_file(self):
#         with open(f"{self.title}.txt", 'w') as file:
#             file.write(self.generate_report())
#



class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate_report(self):
        return f"Report: {self.title} \nContent: {self.content}"

    def generate_md_report(self):
        return f"Report: {self.title} \nContent: {self.content}"

    def generate_json_report(self):
        return f'Report: "{self.title}" \ncontent: {self.content}'

class ReportSaver:
    def save_to_file(self, report_content, filename, file_ext):
        with open(f"{filename}.{file_ext}", 'w') as file:
            file.write(report_content)

class ReportPrinter:
    def print_report(self, report_content):
        print(report_content)


good_report = Report("Good news", "Everybody likes the new movie.")
ReportSaver.save_to_file(report_content=good_report.generate_md_report(),filename= good_report.title, file_ext="md")
ReportPrinter.print_report(good_report.generate_json_report())