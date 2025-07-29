import os
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = 'templates'

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=True)


def build():
    for template_name in env.list_templates(filter_func=lambda x: x.endswith('.html')):
        if template_name == 'base.html':
            continue
        template = env.get_template(template_name)
        active_page = os.path.splitext(template_name)[0]
        if active_page == 'index':
            active_page = 'home'
        html = template.render(active_page=active_page)
        output_path = os.path.join('.', template_name)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Rendered {template_name} -> {output_path}')


if __name__ == '__main__':
    build()
