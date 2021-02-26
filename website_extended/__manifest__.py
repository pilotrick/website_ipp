{
    # Theme information
    'name': 'Webshop - Portal Extended',
    'category': 'Website',
    'version': '1.0',
    'description': """""",

    # Dependencies
    'depends': [
        'website_sale_stock'
    ],

    # Views
    'data': [
        'templates/assets.xml',
        'templates/template.xml',
        'views/stock_warehouse_view.xml'
    ],

    # Technical
    'installable': True,
    'application': True,
}
