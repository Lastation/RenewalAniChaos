import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         RemoveUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

         if (f.loop[cp] == 0) { f.Table_Sin(cp, 45, 50); f.Table_Cos(cp, 45, 50); }
         else if (f.loop[cp] == 1) { f.Table_Sin(cp, 22, 125); f.Table_Cos(cp, 22, 125); }
         else if (f.loop[cp] == 2) { f.Table_Sin(cp, 90, 50); f.Table_Cos(cp, 90, 50); }
         else if (f.loop[cp] == 3) { f.Table_Sin(cp, 67, 125); f.Table_Cos(cp, 67, 125); }

         f.SquareShape(cp, 1, "40 + 1n Guardian", f.CosAngle[cp], f.SinAngle[cp]);
         f.SquareShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
         KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

         if (f.loop[cp] == 1) { f.Table_Sin(cp, 45, 50); f.Table_Cos(cp, 45, 50); }
         else if (f.loop[cp] == 2) { f.Table_Sin(cp, 22, 125); f.Table_Cos(cp, 22, 125); }
         else if (f.loop[cp] == 3) { f.Table_Sin(cp, 90, 50); f.Table_Cos(cp, 90, 50); }

         f.SquareShape(cp, 1, "Kakaru (Twilight)", f.CosAngle[cp], f.SinAngle[cp]);
         KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

         f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Guardian", cp, "Anywhere", Attack, f.location[cp]);

         f.SkillWait(cp, 320);

         f.loop[cp] += 1;

         if (f.loop[cp] == 4)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {       
            var x = 64 - 32 * f.loop[cp];
            var y = 64;

            f.SquareShape(cp, 1, "40 + 1n Guardian", x, y);
            f.SquareShape(cp, 1, "Protoss Dark Archon", x, y);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 8)
         {         
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 3, 32);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 3, 32);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {         
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 5, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 9)
         {         
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 7, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.Table_Sin(cp, 22, 75);
            f.Table_Cos(cp, 22, 75);

            f.SquareShape(cp, 1, "40 + 1n Drone", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 67, 150);
            f.Table_Cos(cp, 67, 150);

            f.SquareShape(cp, 1, "40 + 1n Drone", f.CosAngle[cp], f.SinAngle[cp]);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 960);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 14)
         {         
            f.Table_Sin(cp, 22, 75);
            f.Table_Cos(cp, 22, 75);

            f.SquareShape(cp, 4, "Protoss Dark Templar", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 22 + 45 * f.loop[cp], 150);
            f.Table_Cos(cp, 22 + 45 * f.loop[cp], 150);

            f.SquareShape(cp, 4, "Protoss Dark Templar", f.CosAngle[cp], f.SinAngle[cp]);

            KillUnitAt(All, "Protoss Dark Templar", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 14)
         {         
            f.SkillWait(cp, 320);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}