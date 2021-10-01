from stl import mesh


def find_mins_maxs(obj):
    minx = obj.x.min()
    maxx = obj.x.max()
    miny = obj.y.min()
    maxy = obj.y.max()
    minz = obj.z.min()
    maxz = obj.z.max()
    return minx, maxx, miny, maxy, minz, maxz


def extract(file, sphere_type):
    main_body = mesh.Mesh.from_file(file)
    minx, maxx, miny, maxy, minz, maxz = find_mins_maxs(main_body)
    width = maxx - minx
    length = maxy - miny
    height = maxz - minz
    volume, _, _ = main_body.get_mass_properties()
    surface_area = main_body.areas.sum()

    data = {}
    if sphere_type == 1:
        data = {
            "width": width,
            "length": length,
            "height": height,
        }
    if sphere_type == 2:
        w_int, l_int, h_int = int(width), int(length), int(height)
        diameter = None
        if w_int == l_int or w_int == h_int:
            diameter = width
            if w_int == l_int:
                length = height
        elif l_int == h_int:
            length = width
            diameter = height

        if diameter:
            data = {
                "length": length,
                "diameter": diameter,
            }
        else:
            return {"error": "Please upload a valid round sphere."}
    return {
        **data,
        "volume": volume,
        "surface_area": surface_area,
    }
