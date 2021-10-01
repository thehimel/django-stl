# django-stl

An app to read STL files.

## Terminology

### STL (file format)

According to Wikipedia, STL is a file format native to the stereolithography CAD software created by 3D Systems.
More information can be found [here](https://en.wikipedia.org/wiki/STL_(file_format)).

## Features

- Upload an STL file to the server.
- Server reads the file.
- Server can extract the following data:
  - bounding box with dimensions:
    - length, width, height for square
    - length and diameter for round
  - volume
  - surface area

## Python

- Minimum Python interpreter version is `3.9`.

## Libraries

- `Django` for making the web application.
- `numpy-stl` for reading the STL file.
- `pathlib` to handle file path.
- `pytest` for testing.

## Getting Started

- Clone the repository.
- Create a virtual environment.
  - Windows: `python -m venv venv`
  - Linux: `python3.9 -m venv venv`
- Activate the virtual environment.
  - Windows: `venv\Scripts\activate`
  - Linux: `source venv/bin/activate`
- Install dependencies with `pip install -r requirements.txt`
- Run migration with `python src/manage.py migrate`

## Running the Server

- Run the server with `python src/manage.py runserver`
- By default, the server runs at http://127.0.0.1:8000/

## Usage

- Select a sphere type and upload an STL file.

## Testing

- Run tests with `pytest src`

## Author

- Himel Das

## Acknowledgement

### Citation

- https://pypi.org/project/numpy-stl/
- https://docs.djangoproject.com/en/3.2/topics/http/file-uploads/
- https://www.ordinarycoders.com/blog/article/django-file-image-uploads
- https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html

### Sources

- [300_polygon_sphere_100mm.STL](https://www.thingiverse.com/thing:156207)
- [rectangel.stl](https://www.thingiverse.com/thing:9742)
