import requests


def check_data(cep, address, number, neighborhood, city, uf):
    if not cep or not address or not number or not neighborhood or not city or not uf:
        return 'Existem campos em brancos.'
    return True


def search_cep_in_viacep(cep):
    result = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
    result = result.json()
    if len(result) == 1:
        return None
    result2 = result['cep'].replace('-', '')
    result['cep'] = result2
    return result