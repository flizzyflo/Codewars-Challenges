
class FileNameExtractor:
    def extract_file_name(dirty_file_name: str):
        for index, letter in enumerate(dirty_file_name):
            if letter =="_":
                dirty_file_name = dirty_file_name[index + 1:]
                break
        
        for index, letter in enumerate(dirty_file_name[::-1]):
            if letter ==".":
                dirty_file_name = dirty_file_name[:-index - 1]
                break
        
        return dirty_file_name
        

clear = FileNameExtractor
print(clear.extract_file_name("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION"))

