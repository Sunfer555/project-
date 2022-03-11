from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = "หมวดหมู่"  # เปลี่ยนชื่อ
        verbose_name_plural = "หมวดหมู่"  # เปลี่ยนชื่อ

    name = models.CharField(max_length=255, verbose_name="ชื่อหมวดหมู่")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่เพื่ม")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่อัพเดท")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    class Meta:
        verbose_name = "หมวดหมู่ย่อย"  # เปลี่ยนชื่อ
        verbose_name_plural = "หมวดหมู่ย่อย"  # เปลี่ยนชื่อ

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="ชื่อหมวดหมู่ย่อย")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่เพื่ม")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่อัพเดท")

    def __str__(self) -> str:
        return str(self.category.name) + " : " + self.name

    @property
    def full_name(self):
        return str(self.category.id) + " : " + self.category.name


class Product(models.Model):
    class Meta:
        verbose_name = "สินค้า"  # เปลี่ยนชื่อ
        verbose_name_plural = "สินค้า"  # เปลี่ยนชื่อ

    image = models.ImageField(null=True, blank=True, upload_to='image/')
    category = models.ManyToManyField(SubCategory, verbose_name="หมวดหมู่")
    name = models.CharField(max_length=255, verbose_name="ชื่อ")
    detail = models.TextField(blank=True, null=True, verbose_name="รายละเอียด")  # blank, null ข้อมูลนี้ไม่บังคับให้ใส่
    quantity = models.IntegerField(verbose_name="จำนวนสินค้า")
    price = models.FloatField(max_length=4, blank=True, null=True, verbose_name="ราคา")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="วันที่เพิ่ม")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="วันที่อัพเดท")

    def __str__(self):
        return self.name