import Function as f;

function main(cp)
{
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 8)
         {             
            if (f.loop[cp] == 0)
            {
               f.LineShape(cp, 1, "40 + 1n Mojo", 45, 3, 50, 0);
               f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 3, 50, 0);
            }
            else if (f.loop[cp] == 2)
            {
               RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

               f.LineShape(cp, 1, "40 + 1n Mojo", 45, 5, 50, 0);
               f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 5, 50, 0);
            }
            else if (f.loop[cp] == 4)
            {
               RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

               f.LineShape(cp, 1, "40 + 1n Wraith", 45, 7, 50, 0);
               f.LineShape(cp, 1, " Unit. Hoffnung 25000", 45, 7, 50, 0);
            }
            else if (f.loop[cp] == 6)
            {
               RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

               f.LineShape(cp, 1, "50 + 1n Battlecruiser", 45, 5, 75, 0);
               f.NxNSquareShapeAt(cp, 1, "Protoss Dark Archon", 3, 25, 75, 75);
               f.NxNSquareShapeAt(cp, 1, "Protoss Dark Archon", 3, 25, 150, 150);
               f.NxNSquareShapeAt(cp, 1, "Protoss Dark Archon", 3, 25, 0, 0);
               f.NxNSquareShapeAt(cp, 1, "Protoss Dark Archon", 3, 25, -75, -75);
               f.NxNSquareShapeAt(cp, 1, "Protoss Dark Archon", 3, 25, -150, -150);
            }

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, "Anywhere");

            f.SquareShape(cp, 8, "Vulture Spider Mine", 160 - 40 * f.loop[cp], 160);
            f.SquareShape(cp, 1, "40 + 1n Guardian", 160 - 40 * f.loop[cp], 160);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "Vulture Spider Mine", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 8)
         {             

            if (f.loop[cp] == 0)
            {
               f.Table_Sin(cp, 22 + 45 * (f.loop[cp] % 4), 50);
               f.Table_Cos(cp, 22 + 45 * (f.loop[cp] % 4), 50);

               f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
            }
            else if (f.loop[cp] == 2)
            {
               f.Table_Sin(cp, 22 + 45 * (f.loop[cp] % 4), 100);
               f.Table_Cos(cp, 22 + 45 * (f.loop[cp] % 4), 100);

               f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
            }
            else if (f.loop[cp] == 4)
            {
               f.Table_Sin(cp, 22 + 45 * (f.loop[cp] % 4), 100);
               f.Table_Cos(cp, 22 + 45 * (f.loop[cp] % 4), 100);

               f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
            }
            else if (f.loop[cp] == 6)
            {
               f.Table_Sin(cp, 22 + 45 * (f.loop[cp] % 4), 150);
               f.Table_Cos(cp, 22 + 45 * (f.loop[cp] % 4), 150);

               f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);
               f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
            }

            if (f.loop[cp] % 2 == 0)
            {
               KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

               f.LineShape(cp, 1, " Creep. Dunkelheit", 45, 5, 75, f.loop[cp] * 25);
               f.LineShape(cp, 1, " Creep. Dunkelheit", 225, 5, 75, f.loop[cp] * 25);
               f.LineShape(cp, 8, "Vulture Spider Mine", 45, 5, 75, f.loop[cp] * 25);
               f.LineShape(cp, 8, "Vulture Spider Mine", 225, 5, 75, f.loop[cp] * 25);
               f.LineShape(cp, 1, "40 + 1n Wraith", 45, 7, 50, f.loop[cp] * 25);
               f.LineShape(cp, 1, "40 + 1n Wraith", 225, 7, 50, f.loop[cp] * 25);
            }

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, " Creep. Dunkelheit", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order(" Creep. Dunkelheit", cp, "Anywhere", Attack, f.location[cp]);

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", 160 - 40 * f.loop[cp], 160);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, "Vulture Spider Mine", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            RemoveUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {
            KillUnitAt(All, " Creep. Dunkelheit", "Anywhere", cp);

            f.Table_Sin(cp, 22, 50);
            f.Table_Cos(cp, 22, 50);

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 67, 100);
            f.Table_Cos(cp, 67, 100);

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "40 + 1n Drone", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 22, 100);
            f.Table_Cos(cp, 22, 100);

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 67, 150);
            f.Table_Cos(cp, 67, 150);

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "40 + 1n Drone", f.CosAngle[cp], f.SinAngle[cp]);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 560);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 3)
         {         
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");

            var x = 50 + 50 * f.loop[cp];
            var y = 50 + 50 * f.loop[cp];
            var interval = 50 + 10 * f.loop[cp];

            f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", x, y);
            f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", x - interval, y);
            f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", x, y - interval);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            var x = 150;
            var y = 150;
            var interval = 70;

            f.DoubleShape(cp, 1, "40 + 1n Guardian", x, y);
            f.DoubleShape(cp, 1, "40 + 1n Guardian", x - interval, y);
            f.DoubleShape(cp, 1, "40 + 1n Guardian", x, y - interval);
            f.DoubleShape(cp, 1, "Protoss Dark Archon", x, y);
            f.DoubleShape(cp, 1, "Protoss Dark Archon", x - interval, y);
            f.DoubleShape(cp, 1, "Protoss Dark Archon", x, y - interval);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            var x = 150;
            var y = 150;
            var interval = 70;

            f.DoubleShape(cp, 1, "40 + 1n Wraith", x, y);
            f.DoubleShape(cp, 1, "40 + 1n Wraith", x - interval, y);
            f.DoubleShape(cp, 1, "40 + 1n Wraith", x, y - interval);
            f.DoubleShape(cp, 1, "40 + 1n Ghost", x, y);
            f.DoubleShape(cp, 1, "40 + 1n Ghost", x - interval, y);
            f.DoubleShape(cp, 1, "40 + 1n Ghost", x, y - interval);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }

         else if (f.loop[cp] < 8)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            var x = -50 - 50 * (f.loop[cp] - 5);
            var y = 50 + 50 * (f.loop[cp] - 5);
            var interval = 50 + 10 * (f.loop[cp] - 5);

            f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", x, y);
            f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", x + interval, y);
            f.DoubleShape(cp, 1, " Unit. Hoffnung 25000", x, y - interval);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {         
            var x = -150;
            var y = 150;
            var interval = 70;

            f.DoubleShape(cp, 1, "40 + 1n Guardian", x, y);
            f.DoubleShape(cp, 1, "40 + 1n Guardian", x + interval, y);
            f.DoubleShape(cp, 1, "40 + 1n Guardian", x, y - interval);
            f.DoubleShape(cp, 1, "Protoss Dark Archon", x, y);
            f.DoubleShape(cp, 1, "Protoss Dark Archon", x + interval, y);
            f.DoubleShape(cp, 1, "Protoss Dark Archon", x, y - interval);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 9)
         {         
            var x = -150;
            var y = 150;
            var interval = 70;

            f.DoubleShape(cp, 1, "40 + 1n Wraith", x, y);
            f.DoubleShape(cp, 1, "40 + 1n Wraith", x + interval, y);
            f.DoubleShape(cp, 1, "40 + 1n Wraith", x, y - interval);
            f.DoubleShape(cp, 1, "40 + 1n Ghost", x, y);
            f.DoubleShape(cp, 1, "40 + 1n Ghost", x + interval, y);
            f.DoubleShape(cp, 1, "40 + 1n Ghost", x, y - interval);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 10)
         {
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] < 4)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Wraith", 45 + 45 * f.loop[cp], 7, 50, 0);
            f.LineShape(cp, 1, "Protoss Dark Archon", 45 + 45 * f.loop[cp], 7, 50, 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 7)
         {       
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Wraith", 45, 7, 50, 0);
            f.LineShape(cp, 1, "Protoss Dark Archon", 45, 7, 50, 0);
            f.LineShape(cp, 1, "40 + 1n Wraith", 90, 7, 50, 0);
            f.LineShape(cp, 1, "Protoss Dark Archon", 90, 7, 50, 0);
            f.LineShape(cp, 1, "40 + 1n Wraith", 135, 7, 50, 0);
            f.LineShape(cp, 1, "Protoss Dark Archon", 135, 7, 50, 0);
            f.LineShape(cp, 1, "40 + 1n Wraith", 0, 7, 50, 0);
            f.LineShape(cp, 1, "Protoss Dark Archon", 0, 7, 50, 0);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 4)
      {
         if (f.loop[cp] == 0)
         {         
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 3, 50);
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 3, 50);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 5, 100);
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 5, 100);

            f.EdgeShape(cp, 1, "40 + 1n Ghost", 0, 5, 100);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Ghost", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Ghost", cp, "Anywhere", Attack, f.location[cp]);

            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            f.EdgeShape(cp, 1, "50 + 1n Battlecruiser", 0, 5, 100);
            f.EdgeShape(cp, 1, "50 + 1n Tank", 0, 5, 100);

            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 3, 50);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Ghost", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 5)
      {
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");

         if (Bring(cp, AtLeast, 1, "Protoss Carrier", "[Skill]UseSkill") &&
         Bring(cp, AtLeast, 1, "Protoss Arbiter", "[Skill]UseSkill") && f.step[cp] == 210)
         {
            f.Voice_Routine(cp, 4);
            f.wait[cp] = 0;
            f.count[cp] = 0;
            f.loop[cp] = 0;
            f.step[cp] = 220;
            KillUnitAt(1, "Protoss Arbiter", "[Skill]UseSkill", cp);
            KillUnitAt(1, "Protoss Carrier", "[Skill]UseSkill", cp);
         }
         else {
            f.SkillEnd(cp);
         }

      }
   }
}