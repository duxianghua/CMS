from django.db import models



class Area(models.Model):
	area_id = models.AutoField(primary_key="Ture")
	area_name = models.CharField(max_length=20)

	def __str__(self):
		return self.area_name

class Group(models.Model):
	group_id = models.AutoField(primary_key="Ture")
	group_name = models.CharField(max_length=20)

	def __str__(self):
		return self.group_name

class Host(models.Model):
	host_name = models.CharField(max_length=20)
	area = models.ForeignKey(Area)
	host_lip = models.CharField(max_length=16)
	host_wip = models.CharField(max_length=16,null="Ture")
	group = models.ForeignKey(Group)

	def __str__(self):
		return self.host_lip

class servers_info(models.Model):
	host = models.ForeignKey(Host)
	mem_p = models.IntegerField(null="Ture")
	mem_v = models.IntegerField(null="Ture")
	cpu_models = models.CharField(max_length=20,null="Ture")
	cpu_count = models.IntegerField(null="Ture")
	system_type = models.CharField(max_length=20,null="Ture")
	disk_total = models.IntegerField(null="Ture")
	kernel_version = models.CharField(max_length=32,null="Ture")
	lastupdate = models.DateTimeField()