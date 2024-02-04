class AIPDescriptions:

    @property
    def visited_domains(self):
        return (
            'URL-адрес так же принимает два параметра "from" и "to"'
            '- это временной отврезок, фильтр '
            'по которому будет работать запрос. '
            'Значения устанавливаются в секундах от начала эпохи.\n\n'
            'Пример: /urls/visited_domains?from=1545221231&to=1545217638'
        )

    @property
    def visited_links(self):
        return (
            'При сохранении новой записи, так же сохраняется '
            'время запроса в секундах от начала эпохи, '
            'как время посещения url-адреса'
        )
