"""
Utilitário para servir documentação Swagger na aplicação Flask.
Para usar, adicione estas rotas ao app.py principal.
"""

from flask import jsonify, render_template_string
import yaml


def load_swagger_spec():
    """Carrega a especificação Swagger do arquivo YAML."""
    try:
        with open('swagger.yaml', 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return None

def add_swagger_routes(app):
    """Adiciona rotas para documentação Swagger à aplicação Flask."""
    
    @app.route('/api/docs')
    def swagger_ui():
        """Serve a interface do Swagger UI."""
        template = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Payment System API Documentation</title>
            <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@4.15.5/swagger-ui.css" />
            <style>
                html { box-sizing: border-box; overflow: -moz-scrollbars-vertical; overflow-y: scroll; }
                *, *:before, *:after { box-sizing: inherit; }
                body { margin:0; background: #fafafa; }
            </style>
        </head>
        <body>
            <div id="swagger-ui"></div>
            <script src="https://unpkg.com/swagger-ui-dist@4.15.5/swagger-ui-bundle.js"></script>
            <script src="https://unpkg.com/swagger-ui-dist@4.15.5/swagger-ui-standalone-preset.js"></script>
            <script>
                window.onload = function() {
                    const ui = SwaggerUIBundle({
                        url: '/api/swagger.json',
                        dom_id: '#swagger-ui',
                        deepLinking: true,
                        presets: [
                            SwaggerUIBundle.presets.apis,
                            SwaggerUIStandalonePreset
                        ],
                        plugins: [
                            SwaggerUIBundle.plugins.DownloadUrl
                        ],
                        layout: "StandaloneLayout",
                        tryItOutEnabled: true
                    });
                };
            </script>
        </body>
        </html>
        '''
        return render_template_string(template)
    
    @app.route('/api/swagger.json')
    def swagger_spec():
        """Retorna a especificação Swagger em formato JSON."""
        spec = load_swagger_spec()
        if spec:
            return jsonify(spec)
        else:
            return jsonify({"error": "Swagger specification not found"}), 404

# Exemplo de como adicionar ao app.py principal:
# from swagger_helper import add_swagger_routes
# add_swagger_routes(app)