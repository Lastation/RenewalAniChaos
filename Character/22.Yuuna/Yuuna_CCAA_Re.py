import Function as f;

const s = StringBuffer();
function FlowerShape(cp : TrgPlayer, count, Unit : TrgUnit, i, distance, interval);

function main(cp)
{
   f.BanReturn(cp);
   f.HoldPosition(cp);
   MoveLocation("22.Yuuna_Bozo", f.heroID[cp], cp, "Anywhere");

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {         
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 7, 75);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 7, 75);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            f.NxNSquareShape(cp, 1, "130 + 1n Norad", 3, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 3, 75);
            Order("130 + 1n Norad", cp, "Anywhere", Attack, "Anywhere");
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 11)
         {
            KillUnitAt(1, "130 + 1n Norad", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 11)
         {
            SetSwitch("Recall - Yuuna", Set);

            f.SkillWait(cp, 400);

            f.count[cp] += 1;
            f.loop[cp] = 0;
            f.loopB[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {

         if (f.loop[cp] == 0)
         {         
            f.SkillWait(cp, 1440);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.Voice_Routine(cp, 6);
            FlowerShape(cp, 1, "40 + 1n Mojo", 0, 50, 50);
            FlowerShape(cp, 1, "60 + 1n Siege", 0, 50, 50);
            FlowerShape(cp, 1, "40 + 1n Mojo", 2, 50, 50);
            FlowerShape(cp, 1, "60 + 1n Siege", 2, 50, 50);
            FlowerShape(cp, 1, "40 + 1n Mojo", 3, 50, 50);
            FlowerShape(cp, 1, "60 + 1n Siege", 3, 50, 50);
            GiveUnits(All, "60 + 1n Siege", cp, "Anywhere", P11);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SkillWait(cp, 1120);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            FlowerShape(cp, 1, "40 + 1n Mojo", 1, 50, 50);
            FlowerShape(cp, 1, "60 + 1n Siege", 1, 50, 50);
            FlowerShape(cp, 1, "40 + 1n Mojo", 4, 50, 50);
            FlowerShape(cp, 1, "60 + 1n Siege", 4, 50, 50);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            GiveUnits(All, "60 + 1n Siege", cp, "Anywhere", P11);

            f.SkillWait(cp, 1600);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            f.SkillWait(cp, 560);

            f.count[cp] += 1;
            f.loop[cp] = 0;
            f.loopB[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.Voice_Routine(cp, 7);
            GiveUnits(All, "60 + 1n Siege", P11, "Anywhere", cp);
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 135, 9, 50, 50);
            f.LineShape(cp, 1, "Protoss Dark Archon", 315, 9, 50, 50);
            f.LineShape(cp, 1, "40 + 1n Guardian", 315, 9, 50, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 315, 9, 50, 50);
            f.LineShape(cp, 1, "Protoss Dark Archon", 45, 9, 50, 50);
            f.LineShape(cp, 1, "40 + 1n Guardian", 45, 9, 50, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 45, 9, 50, 50);
            f.LineShape(cp, 1, "Protoss Dark Archon", 225, 9, 50, 50);
            f.LineShape(cp, 1, "40 + 1n Guardian", 225, 9, 50, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 225, 9, 50, 50);
            f.LineShape(cp, 1, "Protoss Dark Archon", 135, 9, 50, 50);
            f.LineShape(cp, 1, "40 + 1n Guardian", 135, 9, 50, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 225, 9, 50, 50);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 135, 9, 50, 50);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 9, 50, 50);
            f.LineShape(cp, 1, " Unit. Hoffnung 25000", 315, 9, 50, 50);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            f.LineShape(cp, 1, "50 + 1n Battlecruiser", 225, 9, 50, 50);
            f.LineShape(cp, 1, "40 + 1n Guardian", 135, 9, 50, 50);
            f.LineShape(cp, 1, "40 + 1n Guardian", 45, 9, 50, 50);
            f.LineShape(cp, 1, "40 + 1n Guardian", 315, 9, 50, 50);
            f.LineShape(cp, 1, "50 + 1n Tank", 225, 9, 50, 50);
            f.LineShape(cp, 1, "50 + 1n Tank", 135, 9, 50, 50);
            f.LineShape(cp, 1, "50 + 1n Tank", 45, 9, 50, 50);
            f.LineShape(cp, 1, "50 + 1n Tank", 315, 9, 50, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {         
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 3, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {         
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SkillWait(cp, 2320);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] < 12)
         {         
            f.Table_Sin(cp, 10 * f.loop[cp], 150 - 5 * f.loop[cp]);
            f.Table_Cos(cp, 10 * f.loop[cp], 150 - 5 * f.loop[cp]);

            f.SquareShape(cp, 8, "Rhynadon (Badlands)", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "Rhynadon (Badlands)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {         
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 5, 75);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 5, 75);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 13)
         {         
            f.NxNSquareShape(cp, 1, "40 + 1n Wraith", 7, 75);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 7, 75);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 14)
         {         
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 7, 75);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 7, 75);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 15)
         {         
            f.NxNSquareShape(cp, 1, "50 + 1n Battlecruiser", 5, 100);
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 5, 100);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 2400);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }

      }
      else if (f.count[cp] == 4)
      {
         SetSwitch("Recall - Yuuna", Clear);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         f.SkillEnd(cp);
      }
   }

   if (f.delayB[cp] == 0)
   {
      if (f.count[cp] == 1)
      {
         if (f.loopB[cp] < 4)
         {
            var x = 50 * f.loopB[cp];
            var y = 200 - 50 * f.loopB[cp];

            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.DotShape(cp, 1, "40 + 1n Wraith", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "40 + 1n Wraith", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] < 7)
         {
            var x = 200 - 50 * (f.loopB[cp] - 4);
            var y = -50 * (f.loopB[cp] - 4);

            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.DotShape(cp, 1, "40 + 1n Wraith", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "40 + 1n Wraith", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] += 1;
         }
         else if (f.loopB[cp] == 7)
         {
            var x = 200 - 50 * (f.loopB[cp] - 4);
            var y = -50 * (f.loopB[cp] - 4);

            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.DotShape(cp, 1, "40 + 1n Wraith", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "40 + 1n Wraith", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loopB[cp] = 0;
         }
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