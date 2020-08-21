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
            var x = 32;
            var y = 32;
            var x2 = 32;
            var y2 = 0;

            f.SquareShape(cp, 1, "40 + 1n Mojo", x, y);
            f.SquareShape(cp, 1, "60 + 1n Archon", x, y);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", x2, y2);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            var x = 64;
            var y = 0;
            var x2 = 64;
            var y2 = 64;

            f.SquareShape(cp, 1, "40 + 1n Mojo", x, y);
            f.SquareShape(cp, 1, "60 + 1n Archon", x, y);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", x2, y2);

            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 2)
         {         
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
            
            var x = 32;
            var y = 0;
            var x2 = 32;
            var y2 = 32;

            f.SquareShape(cp, 1, "Target", x, y);
            f.SquareShape(cp, 1, "40 + 1n Goliath", x, y);
            f.SquareShape(cp, 1, "Kakaru (Twilight)", x2, y2);

            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 3)
         {      
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            f.SquareShape(cp, 1, "Target", 96, 0);
            f.SquareShape(cp, 1, "Target", 64, 32);
            f.SquareShape(cp, 1, "Target", 32, 64);
            f.SquareShape(cp, 1, "60 + 1n Archon", 96, 0);
            f.SquareShape(cp, 1, "60 + 1n Archon", 64, 32);
            f.SquareShape(cp, 1, "60 + 1n Archon", 32, 64);

            f.SquareShape(cp, 1, "40 + 1n Goliath", 32, 32);

            KillUnitAt(All, "Target", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Goliath", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);

            f.EdgeShape(cp, 1, "60 + 1n High Templar", 0, 4, 100);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            var x = 100;
            var y = 150;

            var x2 = 150;
            var y2 = 200;

            f.SquareShape(cp, 1, "60 + 1n High Templar", x, y);
            f.SquareShape(cp, 1, "60 + 1n High Templar", y, x);
            f.SquareShape(cp, 1, "60 + 1n High Templar", x2, y2);
            f.SquareShape(cp, 1, "60 + 1n High Templar", y2, x2);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {         
            f.EdgeShape(cp, 1, "40 + 1n Mojo", 0, 4, 100);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 5, 100);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 7)
         {         
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.EdgeShape(cp, 1, "40 + 1n Mojo", 0, 5, 150);
            f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 7, 150);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 8)
         {        
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.EdgeShape(cp, 1, "60 + 1n Danimoth", 0, 5, 150);
            f.EdgeShape(cp, 1, "50 + 1n Tank", 0, 5, 150);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "50 + 1n Tank", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
            Order("50 + 1n Tank", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 9)
         {
            var x = 100;
            var y = 150;

            f.SquareShape(cp, 1, "40 + 1n Mojo", x, y);
            f.SquareShape(cp, 1, "40 + 1n Mojo", y, x);
            f.SquareShape(cp, 1, "60 + 1n Archon", x, y);
            f.SquareShape(cp, 1, "60 + 1n Archon", y, x);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.EdgeShape(cp, 1, "Target", 45, 5, 100);
            KillUnitAt(All, "Target", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 10)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            var x = 150;
            var y = 200;

            f.SquareShape(cp, 1, "40 + 1n Mojo", x, y);
            f.SquareShape(cp, 1, "40 + 1n Mojo", y, x);
            f.SquareShape(cp, 1, "60 + 1n Archon", x, y);
            f.SquareShape(cp, 1, "60 + 1n Archon", y, x);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.EdgeShape(cp, 1, "Target", 0, 5, 100);
            KillUnitAt(All, "Target", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 11)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);


            var x = 125;
            var y = 175;

            var x2 = 200;
            var y2 = 250;

            f.SquareShape(cp, 1, "60 + 1n Siege", x, y);
            f.SquareShape(cp, 1, "60 + 1n Siege", y, x);
            f.SquareShape(cp, 1, "60 + 1n Siege", x2, y2);
            f.SquareShape(cp, 1, "60 + 1n Siege", y2, x2);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", y, x);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x2, y2);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", y2, x2);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 800);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }


      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {         
            f.Table_Sin(cp, 22 + 45 * f.loop[cp], 75 + 75 * f.loop[cp]);
            f.Table_Cos(cp, 22 + 45 * f.loop[cp], 75 + 75 * f.loop[cp]);

            f.SquareShape(cp, 8, "60 + 1n High Templar", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 160);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.Table_Sin(cp, 22, 75);
            f.Table_Cos(cp, 22, 75);

            f.SquareShape(cp, 4, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 67, 150);
            f.Table_Cos(cp, 67, 150);

            f.SquareShape(cp, 4, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 22, 225);
            f.Table_Cos(cp, 22, 225);

            f.SquareShape(cp, 4, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 67, 300);
            f.Table_Cos(cp, 67, 300);

            f.SquareShape(cp, 4, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            f.Table_Sin(cp, 22, 75);
            f.Table_Cos(cp, 22, 75);

            f.SquareShape(cp, 1, "40 + 1n Drone", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 67, 150);
            f.Table_Cos(cp, 67, 150);

            f.SquareShape(cp, 1, "40 + 1n Drone", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 22, 225);
            f.Table_Cos(cp, 22, 225);

            f.SquareShape(cp, 1, "40 + 1n Drone", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 67, 300);
            f.Table_Cos(cp, 67, 300);

            f.SquareShape(cp, 1, "40 + 1n Drone", f.CosAngle[cp], f.SinAngle[cp]);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 28)
         {      
            f.Table_Sin(cp, 22 + 45 * (f.loop[cp] % 4), 75 + 75 * (f.loop[cp] % 4));
            f.Table_Cos(cp, 22 + 45 * (f.loop[cp] % 4), 75 + 75 * (f.loop[cp] % 4));

            f.SquareShape(cp, 8, "60 + 1n High Templar", f.CosAngle[cp], f.SinAngle[cp]);
            KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 28)
         {         
            KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 4)
         {         
            f.NxNSquareShape(cp, 1, "60 + 1n Danimoth", 3 + 2 * f.loop[cp], 75);
            f.NxNSquareShape(cp, 1, "60 + 1n Archon", 3 + 2 * f.loop[cp], 75);
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);
            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 4)
         {         
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 9, 75);
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 9, 75);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {         
            f.NxNSquareShape(cp, 1, "60 + 1n Danimoth", 9, 75);
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 9, 75);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {         
            KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);

            f.SkillWait(cp, 800);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }


      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}