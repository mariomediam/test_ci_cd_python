from flask_restful import Resource, reqparse

serializador = reqparse.RequestParser(bundle_errors=True)
serializador.add_argument(
    "actividadNombre",
    required=True,
    location="json",
    help="Falta la actividadNombre",
    type=str
)

class ActividadesController(Resource):
    def get(self):
        return {
            "message": None,
            "content": [
                {
                    "actividadId":1,
                    "actividadNombre": "Ir a la playa"
                },
                {
                    "actividadId":2,
                    "actividadNombre": "Cocinar"
                },
                {
                    "actividadId":3,
                    "actividadNombre": "Ir al cumple de mi abuela"
                }
            ]
        }, 201
    
    def post(self):
        data : dict =serializador.parse_args()
        #logica para registrar la actividad en la bd
        actividadCreada = {
            "actividadId":50,
            "actividadNombre": data.get("actividadNombre")
        }
        return {
            "message": "actividad creada exitosamente",
            "content": actividadCreada
        }, 201