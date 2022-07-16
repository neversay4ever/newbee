from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class HoneyCollector(models.Model):
    honey_collector_code = models.CharField(_("采集人编号"), max_length=50, null=True, blank=True)
    honey_collector = models.CharField(_("采集人"), max_length=50, null=True, blank=True)
    collector_phone = models.CharField(_("联系电话"), max_length=50, null=True, blank=True)
    collector_email = models.EmailField(_("邮箱"), max_length=254)
    collector_address = models.CharField(_("地址"), max_length=50, null=True, blank=True)
    collector_note = models.CharField(_("采集人备注"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '蜂蜜采集人信息'
        verbose_name_plural = '蜂蜜采集人信息'
        
    def __str__(self):
        return f'{self.honey_collector}'


class HoneyComposition(models.Model):
    honey_sample_id = models.CharField(_("蜂蜜编号"), max_length=50, null=True, blank=True)
    taxon_species = models.CharField(_("成份物种名"), max_length=50, null=True, blank=True)
    taxon_species_chinese = models.CharField(_("成份物种中文名"), max_length=50, null=True, blank=True)
    abundance_percentage = models.CharField(_("丰度百分比"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '蜂蜜成份信息'
        verbose_name_plural = '蜂蜜成份信息'
        
    def __str__(self):
        return f'{self.honey_sample_id}-{self.taxon_species}'

class HoneyTaxonomy(models.Model):
    taxon_id = models.CharField(_("分类编号"), max_length=50, null=True, blank=True)
    taxon_kindom = models.CharField(_("界"), max_length=50, null=True, blank=True)
    taxon_kindom_chinese = models.CharField(_("界_中文"), max_length=50, null=True, blank=True)
    taxon_phylum = models.CharField(_("门"), max_length=50, null=True, blank=True)
    taxon_phylum_chinese = models.CharField(_("门_中文"), max_length=50, null=True, blank=True)
    taxon_class = models.CharField(_("纲"), max_length=50, null=True, blank=True)
    taxon_class_chinese = models.CharField(_("纲_中文"), max_length=50, null=True, blank=True)
    taxon_order = models.CharField(_("目"), max_length=50, null=True, blank=True)
    taxon_order_chinese = models.CharField(_("目_中文"), max_length=50, null=True, blank=True)
    taxon_family = models.CharField(_("科"), max_length=50, null=True, blank=True)
    taxon_family_chinese = models.CharField(_("科_中文"), max_length=50, null=True, blank=True)
    taxon_genus = models.CharField(_("属"), max_length=50, null=True, blank=True)
    taxon_genus_chinese = models.CharField(_("属_中文"), max_length=50, null=True, blank=True)
    taxon_species = models.CharField(_("种"), max_length=50, null=True, blank=True)
    taxon_species_chinese = models.CharField(_("种_中文"), max_length=50, null=True, blank=True)
    genomic_reference = models.CharField(_("参考基因组类型"), max_length=50, null=True, blank=True)
    data_origin = models.CharField(_("数据来源"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '蜂蜜物种分类信息'
        verbose_name_plural = '蜂蜜物种分类信息'
        
    def __str__(self):
        return f'{self.taxon_id}-{self.taxon_species_chinese}'

class HoneyCollection(models.Model):
    honey_sample_id = models.CharField(_("蜂蜜编号"), max_length=50, null=True, blank=True)
    honey_collector = models.CharField(_("采集人"), max_length=50, null=True, blank=True)
    collection_date = models.DateField(_("采集日期"), auto_now=False, auto_now_add=False)
    continent_ocean = models.CharField(_("大洲"), max_length=50, null=True, blank=True)
    country = models.CharField(_("国家"), max_length=50, null=True, blank=True)
    province = models.CharField(_("省份"), max_length=50, null=True, blank=True)
    city = models.CharField(_("城市"), max_length=50, null=True, blank=True)
    county = models.CharField(_("县"), max_length=50, null=True, blank=True)
    town = models.CharField(_("乡镇"), max_length=50, null=True, blank=True)
    village = models.CharField(_("村"), max_length=50, null=True, blank=True)
    exact_site = models.CharField(_("简要采集地信息"), max_length=50, null=True, blank=True)
    surrounding_environment = models.CharField(_("周边环境"), max_length=50, null=True, blank=True)
    longitude = models.FloatField(_("经度"),null=True, blank=True)
    latitude = models.FloatField(_("纬度"),null=True, blank=True)
    altitude = models.FloatField(_("海拔"),null=True, blank=True)
    honey_bee_origin = models.CharField(_("蜂种"), max_length=50, null=True, blank=True)
    honey_type = models.CharField(_("蜂蜜类型"), max_length=50, null=True, blank=True)
    honey_sample_note = models.CharField(_("样本备注"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '蜂蜜采集信息'
        verbose_name_plural = '蜂蜜采集信息'
        
    def __str__(self):
        return f'{self.honey_sample_id}-{self.honey_collector}'

# combine all into one

class HoneyAll(models.Model):
    honey_sample_id = models.CharField(_("蜂蜜编号"), max_length=50, null=False)
    taxon_species = models.CharField(_("成份物种名"), max_length=50, null=True, blank=True)
    taxon_species_chinese = models.CharField(_("成份物种中文名"), max_length=50, null=True, blank=True)
    abundance_percentage = models.CharField(_("丰度百分比"), max_length=50, null=True, blank=True)

    taxon_id = models.CharField(_("分类编号"), max_length=50, null=True, blank=True)
    taxon_kindom = models.CharField(_("界"), max_length=50, null=True, blank=True)
    taxon_kindom_chinese = models.CharField(_("界_中文"), max_length=50, null=True, blank=True)
    taxon_phylum = models.CharField(_("门"), max_length=50, null=True, blank=True)
    taxon_phylum_chinese = models.CharField(_("门_中文"), max_length=50, null=True, blank=True)
    taxon_class = models.CharField(_("纲"), max_length=50, null=True, blank=True)
    taxon_class_chinese = models.CharField(_("纲_中文"), max_length=50, null=True, blank=True)
    taxon_order = models.CharField(_("目"), max_length=50, null=True, blank=True)
    taxon_order_chinese = models.CharField(_("目_中文"), max_length=50, null=True, blank=True)
    taxon_family = models.CharField(_("科"), max_length=50, null=True, blank=True)
    taxon_family_chinese = models.CharField(_("科_中文"), max_length=50, null=True, blank=True)
    taxon_genus = models.CharField(_("属"), max_length=50, null=True, blank=True)
    taxon_genus_chinese = models.CharField(_("属_中文"), max_length=50, null=True, blank=True)
    taxon_species = models.CharField(_("种"), max_length=50, null=True, blank=True)
    taxon_species_chinese = models.CharField(_("种_中文"), max_length=50, null=True, blank=True)
    genomic_reference = models.CharField(_("参考基因组类型"), max_length=50, null=True, blank=True)
    data_origin = models.CharField(_("数据来源"), max_length=50, null=True, blank=True)

    honey_collector_code = models.CharField(_("采集人编号"), max_length=50, null=True, blank=True)
    honey_collector = models.CharField(_("采集人"), max_length=50, null=True, blank=True)
    collector_phone = models.CharField(_("联系电话"), max_length=50, null=True, blank=True)
    collector_email = models.EmailField(_("邮箱"), max_length=254)
    collector_address = models.CharField(_("地址"), max_length=50, null=True, blank=True)
    collector_note = models.CharField(_("采集人备注"), max_length=50, null=True, blank=True)
    collection_date = models.DateField(_("采集日期"), auto_now=False, auto_now_add=False)
    continent_ocean = models.CharField(_("大洲"), max_length=50, null=True, blank=True)
    country = models.CharField(_("国家"), max_length=50, null=True, blank=True)
    province = models.CharField(_("省份"), max_length=50, null=True, blank=True)
    city = models.CharField(_("城市"), max_length=50, null=True, blank=True)
    county = models.CharField(_("县"), max_length=50, null=True, blank=True)
    town = models.CharField(_("乡镇"), max_length=50, null=True, blank=True)
    village = models.CharField(_("村"), max_length=50, null=True, blank=True)
    exact_site = models.CharField(_("简要采集地信息"), max_length=50, null=True, blank=True)
    surrounding_environment = models.CharField(_("周边环境"), max_length=50, null=True, blank=True)
    longitude = models.FloatField(_("经度"))
    latitude = models.FloatField(_("纬度"))
    altitude = models.FloatField(_("海拔"))
    honey_bee_origin = models.CharField(_("蜂种"), max_length=50, null=True, blank=True)
    honey_type = models.CharField(_("蜂蜜类型"), max_length=50, null=True, blank=True)
    honey_sample_note = models.CharField(_("样本备注"), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = '大表全部蜂蜜信息'
        verbose_name_plural = '大表全部蜂蜜信息'
        
    def __str__(self):
        return f'allinfo-{self.honey_sample_id}'