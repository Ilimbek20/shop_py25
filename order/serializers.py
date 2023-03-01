from rest_framework import serializers
from order.models import Order
from order.send_email import send_order_confirmation_code


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        amount = validated_data.get('amount')
        product = validated_data.get('product')

        if amount > product.amount:
            raise serializers.ValidationError('Нет такого количества бритишка!')
        
        if amount == 0:
            raise serializers.ValidationError('Не обходима заказать хотя бы одну братиш))')
        
        order = Order.objects.create(**validated_data)

        # send_email
        send_order_confirmation_code(order.owner.email, order.activation_code, order.product.title, order.total_price)

        return order