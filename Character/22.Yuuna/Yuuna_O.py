import Function as f;

function FlowerShape(cp : TrgPlayer, count, Unit : TrgUnit, i, distance, interval);

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 4)
         {         
            FlowerShape(cp, 1, "40 + 1n Mojo", 0, 50, 50);
            FlowerShape(cp, 1, "40 + 1n Mojo", 1, 50, 50);
            FlowerShape(cp, 1, "40 + 1n Mojo", 2, 50, 50);
            FlowerShape(cp, 1, "40 + 1n Mojo", 3, 50, 50);
            FlowerShape(cp, 1, "40 + 1n Mojo", 4, 50, 50);
            FlowerShape(cp, 1, "60 + 1n Archon", 0, 50, 50);
            FlowerShape(cp, 1, "60 + 1n Archon", 1, 50, 50);
            FlowerShape(cp, 1, "60 + 1n Archon", 2, 50, 50);
            FlowerShape(cp, 1, "60 + 1n Archon", 3, 50, 50);
            FlowerShape(cp, 1, "60 + 1n Archon", 4, 50, 50);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            FlowerShape(cp, 1, "40 + 1n Guardian", 0, 50, 50);
            FlowerShape(cp, 1, "40 + 1n Guardian", 1, 50, 50);
            FlowerShape(cp, 1, "40 + 1n Guardian", 2, 50, 50);
            FlowerShape(cp, 1, "40 + 1n Guardian", 3, 50, 50);
            FlowerShape(cp, 1, "40 + 1n Guardian", 4, 50, 50);
            FlowerShape(cp, 1, "Protoss Dark Archon", 0, 50, 50);
            FlowerShape(cp, 1, "Protoss Dark Archon", 1, 50, 50);
            FlowerShape(cp, 1, "Protoss Dark Archon", 2, 50, 50);
            FlowerShape(cp, 1, "Protoss Dark Archon", 3, 50, 50);
            FlowerShape(cp, 1, "Protoss Dark Archon", 4, 50, 50);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            SetDeaths(cp, SetTo, 1080, " `UniqueCoolTime");
            SetDeaths(cp, Add, 1, " `UniqueSkill");

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      
      else if (f.count[cp] == 1)
      {
         f.SkillEnd(cp);
      }
   }
}


function FlowerShape(cp : TrgPlayer, count, Unit : TrgUnit, i, distance, interval)
//5장짜리 꽃잎 중 i번째 꽃잎
{
   f.Table_Sin(cp, (72 * i + 90), distance);
   f.Table_Cos(cp, (72 * i + 90), distance);

   var x_o = f.CosAngle[cp];
   var y_o = f.SinAngle[cp];

   f.Table_Sin(cp, ((72 * i + 90) + 30), interval);
   f.Table_Cos(cp, ((72 * i + 90) + 30), interval);

   var x_i1 = f.CosAngle[cp];
   var y_i1 = f.SinAngle[cp];

   f.Table_Sin(cp, ((72 * i + 90) - 30), interval);
   f.Table_Cos(cp, ((72 * i + 90) - 30), interval);

   var x_i2 = f.CosAngle[cp];
   var y_i2 = f.SinAngle[cp];

   var x = x_o;
   var y = y_o;

   f.DotShape(cp, 1, Unit, x, y);

   x = x + x_i1;
   y = y + y_i1;

   f.DotShape(cp, 1, Unit, x, y);

   x = x + x_i1;
   y = y + y_i1;

   f.DotShape(cp, 1, Unit, x, y);

   x = x + x_i2;
   y = y + y_i2;

   f.DotShape(cp, 1, Unit, x, y);

   x = x + x_i2;
   y = y + y_i2;

   f.DotShape(cp, 1, Unit, x, y);

   x = x_o + x_i2;
   y = y_o + y_i2;

   f.DotShape(cp, 1, Unit, x, y);

   x = x + x_i2;
   y = y + y_i2;

   f.DotShape(cp, 1, Unit, x, y);

   x = x + x_i1;
   y = y + y_i1;

   f.DotShape(cp, 1, Unit, x, y);
}