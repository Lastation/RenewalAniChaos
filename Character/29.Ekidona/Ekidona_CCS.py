import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 0);
            f.SquareShapeWithProperty(cp, 1, "40 + 1n Mojo", 50, 0, 1);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] == 2)
         {
            f.SquareShape(cp, 1, "60 + 1n High Templar", 100, 100);
            f.SquareShapeWithProperty(cp, 1, "40 + 1n Mojo", 100, 100, 1);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);
         }

         if (f.loop[cp] == 4)
         {
            f.SquareShape(cp, 1, "60 + 1n High Templar", 150, 0);
            f.SquareShapeWithProperty(cp, 1, "40 + 1n Mojo", 150, 0, 1);

            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 9)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 3)
         {
            f.SquareShape(cp, 8, "Bengalaas (Jungle)", 75, 75);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
         }
         else if (f.loop[cp] < 5)
         {
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", 75, 75);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }
         if (f.loop[cp] == 3)
         {
            f.SquareShape(cp, 1, "60 + 1n Dragoon", 75, 75);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Dragoon", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 11)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         var x = 225 - 75 * f.loop[cp];
         var y = 75 + 75 * f.loop[cp];

         if (f.loop[cp] < 4)
         {
            f.SquareShape(cp, 1, "40 + 1n Gantrithor", x, y);
            f.SquareShape(cp, 1, "60 + 1n Siege", x, y);

            f.LineShape(cp, 1, "Kakaru (Twilight)", 45 * f.loop[cp], 7, 50, 0);
            f.LineShape(cp, 1, "40 + 1n Zergling", 45 * f.loop[cp], 7, 50, 0);

            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Zergling", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }
         if (f.loop[cp] == 6)
         {
            f.EdgeShape(cp, 1, "50 + 1n Tank", 0, 3, 100);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         }
         if (f.loop[cp] == 8)
         {
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 0, 3, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Guardian", 0, 5, 200);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 200);
            f.EdgeShape(cp, 1, "Protoss Reaver", 0, 5, 200);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            ModifyUnitHangarCount(1, All, "Protoss Reaver", CurrentPlayer, "Anywhere");

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "Protoss Reaver", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);

         }
         if (f.loop[cp] == 13)
         {
            KillUnitAt(All, "Protoss Reaver", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 15)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] == 0)
         {
            f.DotShape(cp, 1, "50 + 1n Battlecruiser", 0, 0);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
         }

         if (f.loop[cp] < 6)
         {
            f.Table_Sin(cp, 0, 300 - 50 * f.loop[cp]);
            f.Table_Cos(cp, 0, 300 - 50 * f.loop[cp]);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "Bengalaas (Jungle)", x, y);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);

            f.Table_Sin(cp, 45, 300 - 50 * f.loop[cp]);
            f.Table_Cos(cp, 45, 300 - 50 * f.loop[cp]);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "Bengalaas (Jungle)", x, y);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
         }
         if (f.loop[cp] == 6)
         {
            f.Table_Sin(cp, 0, 100);
            f.Table_Cos(cp, 0, 100);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
            f.SquareShape(cp, 4, "Protoss Reaver", x, y);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            ModifyUnitHangarCount(1, All, "Protoss Reaver", CurrentPlayer, "Anywhere");

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "Protoss Reaver", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
         }
         if (f.loop[cp] == 7)
         {
            f.Table_Sin(cp, 0, 100);
            f.Table_Cos(cp, 0, 100);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "40 + 1n Gantrithor", x, y);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }
         if (f.loop[cp] == 11)
         {
            KillUnitAt(All, "Protoss Reaver", "Anywhere", cp);

            f.Table_Sin(cp, 30, 100);
            f.Table_Cos(cp, 30, 100);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
            f.SquareShape(cp, 4, "Protoss Reaver", x, y);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            ModifyUnitHangarCount(1, All, "Protoss Reaver", CurrentPlayer, "Anywhere");

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "Protoss Reaver", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
         }
         if (f.loop[cp] == 12)
         {
            f.Table_Sin(cp, 0, 100);
            f.Table_Cos(cp, 0, 100);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "40 + 1n Gantrithor", x, y);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }
         if (f.loop[cp] == 16)
         {
            KillUnitAt(All, "Protoss Reaver", "Anywhere", cp);

            f.Table_Sin(cp, 90, 100);
            f.Table_Cos(cp, 90, 100);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
            f.SquareShape(cp, 4, "Protoss Reaver", x, y);
            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            ModifyUnitHangarCount(1, All, "Protoss Reaver", CurrentPlayer, "Anywhere");

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "Protoss Reaver", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
         }
         if (f.loop[cp] == 17)
         {
            f.Table_Sin(cp, 0, 100);
            f.Table_Cos(cp, 0, 100);

            var x = f.CosAngle[cp];
            var y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "40 + 1n Gantrithor", x, y);
            KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 19)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }   


      else if (f.count[cp] == 4)
      {
         KillUnitAt(All, "Protoss Reaver", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}