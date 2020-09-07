import Function as f;

const s = StringBuffer();

function main(cp)
{
   if (Switch("Unique - Milim", Cleared))
   {
      f.HoldPosition(cp);
   }
   f.BanReturn(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            var x = 75;
            var y = 125;

            f.SquareShape(cp, 1, "40 + 1n Mojo", x, y);
            f.SquareShape(cp, 1, "40 + 1n Mojo", y, x);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", x, y);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", y, x);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.EdgeShape(cp, 1, "Target", 45, 5, 100);
            KillUnitAt(All, "Target", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            var x = 125;
            var y = 175;

            f.SquareShape(cp, 1, "40 + 1n Mojo", x, y);
            f.SquareShape(cp, 1, "40 + 1n Mojo", y, x);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", x, y);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", y, x);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.EdgeShape(cp, 1, "Target", 0, 5, 100);
            KillUnitAt(All, "Target", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            var x = 75;
            var y = 125;

            f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", y, x);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            x = 125;
            y = 175;

            f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", y, x);

            f.EdgeShape(cp, 1, "40 + 1n Wraith", 0, 5, 100);
            f.EdgeShape(cp, 1, "40 + 1n Firebat", 0, 3, 100);

            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Firebat", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Firebat", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 7)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.LineShape(cp, 1, "40 + 1n Mojo", 45 * (f.loop[cp] % 4), 5, 64, 0);
            f.LineShape(cp, 1, "Protoss Dark Archon", 45 * (f.loop[cp] % 4), 5, 64, 0);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            Order("40 + 1n Mojo", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            f.Table_Sin(cp, 22, 75);
            f.Table_Cos(cp, 22, 75);

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.Table_Sin(cp, 67, 125);
            f.Table_Cos(cp, 67, 125);

            f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "50 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            f.Table_Sin(cp, 22, 175);
            f.Table_Cos(cp, 22, 175);

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "60 + 1n Archon", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {         
            f.Table_Sin(cp, 67, 225);
            f.Table_Cos(cp, 67, 225);

            f.SquareShape(cp, 1, "40 + 1n Gantrithor", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "50 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);


            f.SkillWait(cp, 160);
            
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.SkillWait(cp, 480);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 4)
         {         
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.Table_Sin(cp, 22 + 45 * (f.loop[cp] % 4), 75);
            f.Table_Cos(cp, 22 + 45 * (f.loop[cp] % 4), 75);

            f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 7, "40 + 1n Zealot", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 8)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.Table_Sin(cp, 22 + 22 * (f.loop[cp] % 4), 225);
            f.Table_Cos(cp, 22 + 22 * (f.loop[cp] % 4), 225);

            f.SquareShape(cp, 1, "80 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "80 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 12)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.Table_Sin(cp, 22 + 22 * (f.loop[cp] % 4), 225);
            f.Table_Cos(cp, 22 + 22 * (f.loop[cp] % 4), 225);

            f.SquareShape(cp, 1, "40 + 1n Wraith", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {         
            RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 640);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "40 + 1n Firebat", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}