


    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns a diccionary of ALL objects """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id """
        if obj:
            self.__objects[obj.__class__.__name__ + "." + obj.id] = obj


    def save(self):
        """serializes __objects to the JSON file (path: _file_path)"""
        with open(FileStorage.__file_path, "w") as buffer:
            json.dumps(FileStorage.__objects, FileStorage.__file_path)

    def reload(self):
        """if the file exist, deserializes the JSON file to __objects"""
        try:
            os.path.isfile(FileStorage.__file_path)
        except Exception as e:
            pass
        else:
            with open(FileStorage.__file_path, 'r') as buffer:
                FileStorage.__objects = json.loads(buffer)
