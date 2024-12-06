from sqlalchemy import (
    Column, ForeignKey, Integer, Text, Date, Numeric, CheckConstraint, Index
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    cedula = Column(Text, unique=True, nullable=False)
    nombre = Column(Text, nullable=False)
    correo = Column(Text, nullable=False, index=True)
    contraseña = Column(Text, nullable=False)
    rol = Column(Text, CheckConstraint("rol IN ('estudiante', 'administrador')"), nullable=False)
    
    estudiante = relationship("Estudiante", back_populates="usuario", uselist=False)

class Estudiante(Base):
    __tablename__ = "estudiantes"
    
    id_estudiante = Column(Integer, ForeignKey("usuarios.id_usuario"), primary_key=True)
    telefono = Column(Text, nullable=True)
    direccion = Column(Text, nullable=True)
    fecha_registro = Column(Date, nullable=False)
    estado = Column(Text, CheckConstraint("estado IN ('activo', 'inactivo')"), nullable=False)
    
    usuario = relationship("Usuario", back_populates="estudiante")
    preferencias = relationship("PreferenciaAcademica", back_populates="estudiante")
    pagos = relationship("Pago", back_populates="estudiante")
    documentos = relationship("Documento", back_populates="estudiante")
    evaluaciones = relationship("Evaluacion", back_populates="estudiante")

class ProgramaAcademico(Base):
    __tablename__ = "programas_academicos"
    
    id_programa = Column(Integer, primary_key=True, autoincrement=True)
    nombre_programa = Column(Text, nullable=False)
    descripcion = Column(Text, nullable=True)
    
    preferencias_principal = relationship("PreferenciaAcademica", foreign_keys="PreferenciaAcademica.id_programa_principal", back_populates="programa_principal")
    preferencias_secundario = relationship("PreferenciaAcademica", foreign_keys="PreferenciaAcademica.id_programa_secundario", back_populates="programa_secundario")

class PreferenciaAcademica(Base):
    __tablename__ = "preferencias_academicas"
    
    id_preferencia = Column(Integer, primary_key=True, autoincrement=True)
    id_estudiante = Column(Integer, ForeignKey("estudiantes.id_estudiante"), nullable=False)
    id_programa_principal = Column(Integer, ForeignKey("programas_academicos.id_programa"), nullable=False)
    id_programa_secundario = Column(Integer, ForeignKey("programas_academicos.id_programa"), nullable=True)
    
    estudiante = relationship("Estudiante", back_populates="preferencias")
    programa_principal = relationship("ProgramaAcademico", foreign_keys=[id_programa_principal], back_populates="preferencias_principal")
    programa_secundario = relationship("ProgramaAcademico", foreign_keys=[id_programa_secundario], back_populates="preferencias_secundario")

class Pago(Base):
    __tablename__ = "pagos"
    
    id_pago = Column(Integer, primary_key=True, autoincrement=True)
    id_estudiante = Column(Integer, ForeignKey("estudiantes.id_estudiante"), nullable=False)
    monto = Column(Numeric(10, 2), nullable=False)
    fecha_pago = Column(Date, nullable=False)
    estado = Column(Text, CheckConstraint("estado IN ('pendiente', 'completado')"), nullable=False)
    
    estudiante = relationship("Estudiante", back_populates="pagos")

class Documento(Base):
    __tablename__ = "documentos"
    
    id_documento = Column(Integer, primary_key=True, autoincrement=True)
    id_estudiante = Column(Integer, ForeignKey("estudiantes.id_estudiante"), nullable=False)
    tipo_documento = Column(Text, nullable=False)
    ruta_archivo = Column(Text, nullable=False)
    estado = Column(Text, nullable=False)
    
    estudiante = relationship("Estudiante", back_populates="documentos")

class Evaluacion(Base):
    __tablename__ = "evaluaciones"
    
    id_evaluacion = Column(Integer, primary_key=True, autoincrement=True)
    id_estudiante = Column(Integer, ForeignKey("estudiantes.id_estudiante"), nullable=False)
    fecha_evaluacion = Column(Date, nullable=False)
    resultado = Column(Text, CheckConstraint("resultado IN ('aprobado', 'rechazado')"), nullable=False)
    
    estudiante = relationship("Estudiante", back_populates="evaluaciones")

# ÍNDICES
Index("idx_usuarios_cedula", Usuario.cedula)
Index("idx_estudiantes_estado", Estudiante.estado)
Index("idx_pagos_estado", Pago.estado)
