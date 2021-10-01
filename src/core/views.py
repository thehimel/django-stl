from django.shortcuts import render
from core.forms import UploadFileForm
from core.utilities import extract
from django.core.files.storage import FileSystemStorage


def index(request):
    context = {"form": UploadFileForm()}
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            sphere_type = int(form.cleaned_data['sphere_type'])
            uploaded_file = request.FILES["file"]
            if uploaded_file.name.lower().endswith(".stl"):
                fss = FileSystemStorage()
                filename = fss.save(uploaded_file.name, uploaded_file)
                output = extract(fss.path(filename), sphere_type)
                if "error" in output:
                    context["error"] = output["error"]
                else:
                    context["data"] = {
                        "file_name": uploaded_file.name,
                        **output
                    }
                fss.delete(filename)
            else:
                context["error"] = "Please upload a valid .stl file."
            context["form"] = form
    return render(request=request, template_name="upload.html", context=context)
