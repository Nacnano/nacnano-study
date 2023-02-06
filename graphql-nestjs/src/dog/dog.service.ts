import { Injectable } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';
import { CreateDogInput, UpdateDogInput } from 'src/types/graphql';

@Injectable()
export class DogService {
  constructor(private prisma: PrismaService) {}

  create({ name }: CreateDogInput) {
    return this.prisma.dog.create({
      data: {
        name,
      },
    });
  }

  findAll() {
    return this.prisma.dog.findMany();
  }

  findOne(id: number) {
    return this.prisma.dog.findUnique({
      where: { id },
      select: { name: true, id: true },
    });
  }

  update(id: number, { name }: UpdateDogInput) {
    return this.prisma.dog.update({
      where: { id },
      data: {
        name,
      },
    });
  }

  remove(id: number) {
    return this.prisma.dog.delete({
      where: { id },
    });
  }
}
