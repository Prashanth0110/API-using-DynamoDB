def query_items(self, resource_name, partition_key_name, partition_key_value, sort_key_name=None, sort_key_value=None, sort_key_operator=None, filter_dict = None, index_name=None):
        table_name = constants.resource_table_dict[resource_name]
        table = self.connection.Table(table_name)
        self.index_name = index_name
        if sort_key_name:
            if sort_key_operator == 'eq':
                response = self.query_items_eq(
                    table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, index_name)
            elif sort_key_operator == 'gt':
                response = self.query_items_gt(
                    table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, index_name)
            elif sort_key_operator == 'gte':
                response = self.query_items_eq(
                    table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, index_name)
            elif sort_key_operator == 'lt':
                response = self.query_items_lt(
                    table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, index_name)
            elif sort_key_operator == 'lte':
                response = self.query_items_lte(
                    table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, index_name)
            elif sort_key_operator == 'begins with':
                response = self.query_items_begins_with(
                    table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, filter_dict, index_name)
            elif sort_key_operator == 'between':
                response = self.query_items_between(
                    table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, index_name)
                
        else:
            if index_name:
                response = table.query(
                    IndexName=index_name,
                    KeyConditionExpression=Key(
                        partition_key_name).eq(partition_key_value)
                )
            else:
                response = table.query(
                    KeyConditionExpression=Key(
                        partition_key_name).eq(partition_key_value)
                )
        return response

    def query_items_eq(self, table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, index_name=None):
        if index_name:
            response = table.query(
                IndexName=index_name,
                KeyConditionExpression=Key(partition_key_name).eq(partition_key_value) &
                Key(sort_key_name).eq(sort_key_value)
            )
        else:
            response = table.query(
                KeyConditionExpression=Key(partition_key_name).eq(
                    partition_key_value) & Key(sort_key_name).eq(sort_key_value)
            )
        return response

    def query_items_gt(self, table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, sort_key_operator, index_name=None):
        if index_name:
            response = table.query(
                IndexName=index_name,
                KeyConditionExpression=Key(partition_key_name).eq(partition_key_value) &
                Key(sort_key_name).gt(sort_key_value)
            )
        else:
            response = table.query(
                KeyConditionExpression=Key(partition_key_name).eq(
                    partition_key_value) & Key(sort_key_name).gt(sort_key_value)
            )
        return response

    def query_items_gte(self, table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, sort_key_operator, index_name=None):
        if index_name:
            response = table.query(
                IndexName=index_name,
                KeyConditionExpression=Key(partition_key_name).eq(partition_key_value) &
                Key(sort_key_name).gte(sort_key_value)
            )
        else:
            response = table.query(
                KeyConditionExpression=Key(partition_key_name).eq(
                    partition_key_value) & Key(sort_key_name).gte(sort_key_value)
            )
        return response

    def query_items_lte(self, table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, sort_key_operator, index_name=None):
        if index_name:
            response = table.query(
                IndexName=index_name,
                KeyConditionExpression=Key(partition_key_name).eq(partition_key_value) &
                Key(sort_key_name).lte(sort_key_value)
            )
        else:
            response = table.query(
                KeyConditionExpression=Key(partition_key_name).eq(
                    partition_key_value) & Key(sort_key_name).lte(sort_key_value)
            )
        return response

    def query_items_lt(self, table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, sort_key_operator, index_name=None):
        if index_name:
            response = table.query(
                IndexName=index_name,
                KeyConditionExpression=Key(partition_key_name).eq(partition_key_value) &
                Key(sort_key_name).lt(sort_key_value)
            )
        else:
            response = table.query(
                KeyConditionExpression=Key(partition_key_name).eq(
                    partition_key_value) & Key(sort_key_name).lt(sort_key_value)
            )
        return response


    def query_items_begins_with(self, table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, filters_dict=None, index_name=None):
        if(filters_dict):           
            if index_name:
                response = table.query(
                    IndexName=index_name,
                    KeyConditionExpression=Key(partition_key_name).eq(partition_key_value) &
                    Key(sort_key_name).begins_with(sort_key_value),
                    FilterExpression = add_expressions(filters_dict)
                )
            else:
                response = table.query(
                    KeyConditionExpression=Key(partition_key_name).eq(partition_key_value) &
                    Key(sort_key_name).begins_with(sort_key_value),
                    FilterExpression = add_expressions(filters_dict)
                )
            
        else:
            if index_name:
                response = table.query(
                    IndexName=index_name,
                    KeyConditionExpression=Key(partition_key_name).eq(partition_key_value) &
                    Key(sort_key_name).lt(sort_key_value)
                )
            else:
                response = table.query(
                    KeyConditionExpression=Key(partition_key_name).eq(
                        partition_key_value) & Key(sort_key_name).begins_with(sort_key_value)
                )
        return response


    def query_items_between(self, table, partition_key_name, partition_key_value, sort_key_name, sort_key_value, sort_key_operator, index_name=None):
        x = sort_key_value.split(',')

        if index_name:
            response = table.query(
                IndexName=index_name,
                KeyConditionExpression=Key(partition_key_name).eq(partition_key_value) &
                Key(sort_key_name).between(x[0], x[1])
            )
        else:
            response = table.query(
                KeyConditionExpression=Key(
                    partition_key_name).eq(partition_key_value)
                & Key(sort_key_name).between(x[0], x[1])
            )
        return response

    #Use when result_data>1MB in Dynamodb query 
    def query_items_pagination(self, resource_name, partition_key_name, partition_key_value, index_name=None):
        table_name = constants.resource_table_dict[resource_name]
        paginator = self.connection.get_paginator('query')
        
        if index_name:
            response = paginator.paginate(TableName = table_name, IndexName = index_name, KeyConditionExpression="#partition_key_name=:partition_key_value", 
                                                ExpressionAttributeNames={"#partition_key_name":partition_key_name},
                                                ExpressionAttributeValues={":partition_key_value":{"S": partition_key_value}},
                                                PaginationConfig={'MaxItems': 100000})
        else:
            response = paginator.paginate(TableName = table_name, KeyConditionExpression="#partition_key_name=:partition_key_value", 
                                                ExpressionAttributeNames={"#partition_key_name":partition_key_name},
                                                ExpressionAttributeValues={":partition_key_value":{"S": partition_key_value}},
                                                PaginationConfig={'MaxItems': 100000})
        return response


    def put_item(self, resource_name, json_item):
        table_name = constants.resource_table_dict[resource_name]
        table = self.connection.Table(table_name)
        response = table.put_item(Item=json_item)
        return response


    def update_item(self, resource_name, key, json_item_all, return_values="UPDATED_NEW"):
        remove_attr = {}
        json_item = {}
        for p, v in json_item_all.items():
            if v ==None:
                remove_attr[p] = v
            else:
                json_item[p] = v

        if len(remove_attr) > 0:
            self.delete_attr(resource_name, key, remove_attr)

        table_name = constants.resource_table_dict[resource_name]
        table = self.connection.Table(table_name)

        update_expression = 'SET {}'.format(','.join(
            f"#{ str(p.replace('.', '.#')) if '.' in p else p} = :{p.replace('.','')}" for p in json_item))
        expression_attribute_values = {
            f":{p.replace('.','')}": v for p, v in json_item.items()}
        
        expression_attribute_names = {}
        for p in json_item:
            if not '.' in p:
                expression_attribute_names.update({f"#{p}": p})
            else:
                nested_elements = p.split('.')
                for nested_element in nested_elements:
                    nested_attribute_name = { f"#{nested_element}": nested_element}
                    expression_attribute_names.update(nested_attribute_name)    

        response = table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ExpressionAttributeNames=expression_attribute_names,
            ReturnValues=return_values
        )
        return response



    def delete_attr(self, resource_name, key, remove_attr, return_values="UPDATED_NEW"):

        table_name = constants.resource_table_dict[resource_name]
        table = self.connection.Table(table_name)

        update_expression = 'REMOVE {}'.format(','.join(
            f"#{str(p.replace('.', '.#')) if '.' in p else p}" for p in remove_attr))
        print(f"Remove updated expression:{update_expression}")
        expression_attribute_names = {}
        for p in remove_attr:
            if not '.' in p:
                expression_attribute_names.update({f"#{p}": p})
            else:
                nested_elements = p.split('.')
                for nested_element in nested_elements:
                    nested_attribute_name = {f"#{nested_element}": nested_element}
                    expression_attribute_names.update(nested_attribute_name)

        response = table.update_item(
            Key=key,
            UpdateExpression=update_expression,
            ExpressionAttributeNames=expression_attribute_names,
            ReturnValues='ALL_NEW'
        )
        return response
        

    def delete_item(self, resource_name, key):
        table_name = constants.resource_table_dict[resource_name]
        table = self.connection.Table(table_name)
        response = table.delete_item(
            Key=key
        )
        return response